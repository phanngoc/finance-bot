Finance Bot
# Finance Bot

This project is a comprehensive solution for building and interacting with a knowledge graph that integrates and connects information extracted from both textual and visual data. The project leverages Docker for containerization and includes various components such as a crawler, Neo4j database, and multiple Jupyter notebooks for research and development.

## Table of Contents
- [Finance Bot](#finance-bot)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Project Structure](#project-structure)
  - [Usage](#usage)
    - [Crawler](#crawler)
    - [Neo4j Database](#neo4j-database)
    - [Research Notebooks](#research-notebooks)
  - [Research](#research)
  - [Contributing](#contributing)
  - [License](#license)

## Getting Started

### Prerequisites
- Docker
- Docker Compose
- Node.js
- Python 3.10.3

### Installation
1. Clone the repository
2. Set up environment variables in `.env` file
3. Build and run the Docker containers

## Project Structure
```
.DS_Store
.env
.gitignore
data/
    bao-cao-tai-chinh/
    bao-chi/
docker-compose.yml
documents/
    doc.md
    learn.md
    query.md
my-crawler/
    .dockerignore
    .gitignore
    Dockerfile
    package.json
    README.md
    src/
neo4j_db/
    data/
    import/
    logs/
    plugins/
output/
README.md
research/
    __pycache__/
    .gitignore
    config.py
    kg_agent_llama.ipynb
    kg_agent.ipynb
    lib/
    neo4j-query.ipynb
    output/
    parse_pdf.ipynb
    storage/
    vector-graphdynamic.ipynb
    vector-graphstore.ipynb
roadmap.md
spec/
test.ipynb
```

## Usage

### Crawler
The crawler is set up using PlaywrightCrawler and can be built and run using Docker.

1. Navigate to the `my-crawler` directory:
    ```bash
    cd my-crawler
    ```
2. Build the Docker image:
    ```bash
    docker build -t my-crawler .
    ```
3. Run the crawler:
    ```bash
    docker run my-crawler
    ```

### Neo4j Database
The Neo4j database is used to store the knowledge graph.

1. Access the Neo4j database:
    ```bash
    http://localhost:7474
    ```
2. Use the default credentials:
    - Username: `neo4j`
    - Password: `ttt@123ASD`

### Research Notebooks
The research directory contains multiple Jupyter notebooks for developing and interacting with the knowledge graph.

1. Start Jupyter Notebook:
    ```bash
    jupyter notebook
    ```
2. Open the desired notebook from the `research` directory.

## Research
The project includes various research notebooks that demonstrate the creation and querying of a multimodal knowledge graph. Key notebooks include:
- `kg_agent_llama.ipynb`
- `kg_agent.ipynb`
- `vector-graphdynamic.ipynb`
- `vector-graphstore.ipynb`

## Contributing
Contributions are welcome! Please read the `CONTRIBUTING.md` for guidelines on how to contribute to this project.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.


For more information, check out this [article](https://towardsdatascience.com/stop-guessing-and-measure-your-rag-system-to-drive-real-improvements-bfc03f29ede3).
