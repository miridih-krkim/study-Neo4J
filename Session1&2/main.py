from langchain_neo4j import Neo4jGraph
from dotenv import load_dotenv
import os

load_dotenv()

#Neo4j 연결 정보
neo4j_url = os.getenv("NEO4J_URI")
neo4j_username = os.getenv("NEO4J_USERNAME")
neo4j_password = os.getenv("NEO4J_PASSWORD")


#그래프 객체 생성
graph = Neo4jGraph(
    url=neo4j_url,
    username=neo4j_username,
    password=neo4j_password
)



def main():
    result = graph.query("MATCH (n) RETURN count(n) as node_count")
    print(f"Neo4j 데이터베이스 내 노드 수 : {result[0]['node_count']}")


if __name__ == "__main__":
    main()
