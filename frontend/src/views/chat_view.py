# views/chat_view.py
# Responsável pela implementação dos componentes visuais do Streamlit

import streamlit as st
from ..drivers.ollama_driver import send_prompt_to_ollama


def render_chat_view():
    """
    Renderiza todos os componentes visuais do Rocket Chat:
    - Título do chat
    - Área de exibição de mensagens
    - Campo de texto para o prompt
    - Botão de confirmação para envio
    """

    # -------------------------------------------------------
    # Componente: Título do chat
    # -------------------------------------------------------
    st.title("🚀 Rocket Chat")
    st.divider()
    # -------------------------------------------------------
    # Componente: Campo de texto para inserir o prompt
    # -------------------------------------------------------
    prompt = st.text_area(
        label="Mensagem",
        placeholder="Digite sua mensagem aqui...",
        height=120,
        key="prompt_input"
    )

    # -------------------------------------------------------
    # Componente: Botão de confirmação para enviar o prompt
    # -------------------------------------------------------
    send_button = st.button("Enviar 🚀", use_container_width=True)

    # -------------------------------------------------------
    # Componente: Área de exibição de mensagens
    # Exibe o histórico completo: mensagem do usuário seguida
    # da resposta da LLM
    # -------------------------------------------------------
    for message in st.session_state.messages:
        if message["role"] == "user":
            # Mensagem do usuário alinhada à direita com avatar
            with st.chat_message("user"):
                st.markdown(message["content"])
        else:
            # Resposta da LLM alinhada à esquerda com avatar
            with st.chat_message("assistant"):
                st.markdown(message["content"])

    st.divider()

    # -------------------------------------------------------
    # Lógica de envio: acionada ao clicar no botão
    # -------------------------------------------------------
    if send_button:
        # Valida se o campo de prompt não está vazio
        if not prompt.strip():
            st.warning("⚠️ Por favor, digite uma mensagem antes de enviar.")
            return

        # Armazena a mensagem do usuário no histórico de sessão
        st.session_state.messages.append({
            "role": "user",
            "content": prompt.strip()
        })

        # Exibe indicador de carregamento enquanto aguarda a LLM
        with st.spinner("Aguardando resposta da LLM..."):
            # Envia o prompt para a LLM via driver do Ollama
            llm_response = send_prompt_to_ollama(prompt.strip())

        # Armazena a resposta da LLM no histórico de sessão
        st.session_state.messages.append({
            "role": "assistant",
            "content": llm_response
        })

        # Recarrega a página para exibir as novas mensagens e limpar o campo
        st.rerun()