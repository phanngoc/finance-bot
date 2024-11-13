import re
from llama_index.core.graph_stores import SimplePropertyGraphStore
import networkx as nx
from graspologic.partition import hierarchical_leiden
from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage


class GraphRAGStore(SimplePropertyGraphStore):
    community_summary = {}
    max_cluster_size = 5

    def generate_community_summary(self, text):
        llm = OpenAI(model="gpt-4o-mini")
        """Generate summary for a given text using an LLM."""
        messages = [
            ChatMessage(
                role="system",
                content=(
                    "Bạn được cung cấp một tập hợp các mối quan hệ từ một đồ thị tri thức, mỗi mối quan hệ được biểu diễn dưới dạng "
                    "entity1->entity2->relation->relationship_description. Nhiệm vụ của bạn là tạo ra một bản tóm tắt về các mối quan hệ này. "
                    "Bản tóm tắt nên bao gồm tên của các thực thể liên quan và một bản tổng hợp ngắn gọn về các mô tả mối quan hệ. "
                    "Mục tiêu là nắm bắt các chi tiết quan trọng và liên quan nhất để làm nổi bật bản chất và ý nghĩa của mỗi mối quan hệ. "
                    "Đảm bảo rằng bản tóm tắt là mạch lạc và tích hợp thông tin theo cách nhấn mạnh các khía cạnh chính của các mối quan hệ."
                ),
            ),
            ChatMessage(role="user", content=text),
        ]
        response = llm.chat(messages)
        clean_response = re.sub(r"^assistant:\s*", "", str(response)).strip()
        return clean_response

    def build_communities(self):
        """Builds communities from the graph and summarizes them."""
        nx_graph = self._create_nx_graph()
        community_hierarchical_clusters = hierarchical_leiden(
            nx_graph, max_cluster_size=self.max_cluster_size
        )
        community_info = self._collect_community_info(
            nx_graph, community_hierarchical_clusters
        )
        self._summarize_communities(community_info)

    def _create_nx_graph(self):
        """Converts internal graph representation to NetworkX graph."""
        # print('self.graph.relations.values()', self.graph.relations.values())
        nx_graph = nx.Graph()
        for node in self.graph.nodes.values():
            nx_graph.add_node(str(node))
        for relation in self.graph.relations.values():
            print('relation:', relation.source_id, ",", relation.target_id, ",", relation.label)
            nx_graph.add_edge(
                relation.source_id,
                relation.target_id,
                relationship=relation.label,
                description=relation.properties["relationship_description"],
            )
        return nx_graph

    def filter_nodes_by_name(self, nx_graph, name_filter):
        """Filter nodes by name containing the given filter string."""
        filtered_nodes = [node for node in nx_graph.nodes if name_filter.lower() in node.lower()]
        for node in filtered_nodes:
            print('filter_nodes_by_name:node:', node.lower())
        filtered_graph = nx_graph.subgraph(filtered_nodes)
        relations = []
        for u, v, data in filtered_graph.edges(data=True):
            print('u:', u, 'v:', v, 'data:', data)
            relations.append({
                'source': u,
                'target': v,
                'relationship': data.get('relationship'),
                'description': data.get('description')
            })
        
        return filtered_graph, relations

    def get_graph(self):
        """Returns the graph."""
        return self.graph

    def visualize_graph(self, filter_query=None):
        """Visualize the graph using NetworkX."""
        print("Visualizing graph...", filter_query)
        nx_graph = self._create_nx_graph()
        if filter_query:
            nx_graph_sub, relations = self.filter_nodes_by_name(nx_graph, filter_query)
            print('relations', relations)

            pos = nx.spring_layout(nx_graph_sub)
            nx.draw(nx_graph_sub, pos, with_labels=True, font_weight="bold")
            edge_labels = nx.get_edge_attributes(nx_graph_sub, "relationship")
            print('edge_labels', edge_labels)
            nx.draw_networkx_edge_labels(nx_graph_sub, pos, edge_labels=edge_labels)
        
        return nx_graph_sub

    def _collect_community_info(self, nx_graph, clusters):
        """Collect detailed information for each node based on their community."""
        community_mapping = {item.node: item.cluster for item in clusters}
        community_info = {}
        for item in clusters:
            cluster_id = item.cluster
            node = item.node
            if cluster_id not in community_info:
                community_info[cluster_id] = []

            for neighbor in nx_graph.neighbors(node):
                if community_mapping[neighbor] == cluster_id:
                    edge_data = nx_graph.get_edge_data(node, neighbor)
                    if edge_data:
                        detail = f"{node} -> {neighbor} -> {edge_data['relationship']} -> {edge_data['description']}"
                        community_info[cluster_id].append(detail)
        return community_info

    def _summarize_communities(self, community_info):
        """Generate and store summaries for each community."""
        for community_id, details in community_info.items():
            print('_summarize_communities:details', details)
            details_text = (
                "\n".join(details) + "."
            )  # Ensure it ends with a period
            self.community_summary[
                community_id
            ] = self.generate_community_summary(details_text)

    def get_community_summaries(self):
        """Returns the community summaries, building them if not already done."""
        if not self.community_summary:
            self.build_communities()
        return self.community_summary