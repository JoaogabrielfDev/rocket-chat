# drivers/ollama_driver.py
# Responsável pela utilização da biblioteca Requests para comunicação com o Ollama

import requests

# URL padrão da API do Ollama rodando localmente
OLLAMA_API_URL = "http://localhost:3001/generate"


def send_prompt_to_ollama(prompt: str) -> str:
    """
    Envia o prompt para a LLM hospedada no Ollama via biblioteca Requests.

    Args:
        prompt (str): Texto enviado pelo usuário.

    Returns:
        str: Resposta gerada pela LLM ou mensagem de erro.
    """

    # Corpo da requisição conforme a API do Ollama
    payload = {
        "user_prompt": prompt,
    }

    try:
        # Envio da requisição POST para a API do Ollama usando Requests
        response = requests.post(
            OLLAMA_API_URL,
            json=payload,
            timeout=120  # Timeout de 120 segundos para respostas longas
        )

        # Verifica se a requisição foi bem-sucedida
        response.raise_for_status()

        # Extrai o campo "response" do JSON retornado pelo Ollama
        data = response.json()
        return data.get("response", "Resposta não encontrada.")

    except requests.exceptions.ConnectionError:
        # Erro de conexão: Ollama não está rodando ou inacessível
        return "❌ Erro: Não foi possível conectar ao Ollama. Verifique se o serviço está em execução."

    except requests.exceptions.Timeout:
        # Timeout na requisição
        return "❌ Erro: A requisição ao Ollama excedeu o tempo limite."

    except requests.exceptions.HTTPError as e:
        # Erro HTTP retornado pelo servidor Ollama
        return f"❌ Erro HTTP: {e}"

    except Exception as e:
        # Qualquer outro erro inesperado
        return f"❌ Erro inesperado: {e}"