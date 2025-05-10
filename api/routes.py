from flask import jsonify, request
from ai.llm import LLM
from ai.rag import RAG
from ai.compliance import check_compliance

llm = LLM()
rag = RAG()

def init_routes(app):
    """
    Initialize the API routes for the Flask application.

    This function sets up the following routes:
    - POST /query: Accepts a JSON payload containing a 'query' field. It processes the query using the RAG model to retrieve context and the LLM to generate a predictive response. The response is checked for compliance, and appropriate feedback is returned.
    - GET /monitor: Returns a placeholder response intended to provide query/response logs from PostgreSQL.

    Args:
        app (Flask): The Flask application instance to which the routes are added.
    """

    @app.route("/query", methods=["POST"])
    def query():
        """
        Handle POST requests to the /query endpoint.

        This function processes a JSON payload containing a 'query' field. It queries the RAG model to retrieve the most relevant context,
        generates a predictive response using the LLM, and checks the response for compliance. If the response is non-compliant, it returns
        a blocked message.

        Returns:
            Response: A JSON response containing the original query and the generated response text.
        """
        data = request.get_json()
        query_text = data.get("query")
        context = rag.query(query_text)
        response = llm.predict(" ".join(context + [query_text]))
        response_text = "Compliant response" if response[1] > 0.5 else "Non-compliant"
        if not check_compliance(response_text):
            response_text = "Response blocked for compliance."
        return jsonify({"query": query_text, "response": response_text})

    @app.route("/monitor", methods=["GET"])
    def monitor():
        # Placeholder: Return query/response logs from PostgreSQL
        """
        Handle GET requests to the /monitor endpoint.

        This function is a placeholder that returns a JSON response containing an empty list.
        In a future implementation, this endpoint should return query/response logs from PostgreSQL.

        Returns:
            Response: A JSON response containing a list of query/response logs.
        """
        return jsonify({"logs": []})