import streamlit as st

# Configuração da página para ficar bonita no celular
st.set_page_config(page_title="Quiz", page_icon="🧠", layout="centered")

st.title("🧠 Quiz de Conhecimentos")
st.markdown("Teste seu conhecimemto biblico!")

# Criando um formulário para organizar o envio
with st.form("quiz_form"):
    q1 = st.radio(
        "1. De acordo com o livro de Gênesis, em qual dia da criação Deus criou o sol, a lua e as estrelas?",
        ("Terceiro dia", "Primeiro dia", "Quarto dia", "Sexto dia"),
        index=None
    )

    q2 = st.radio(
        "2. Qual era o nome do sucessor de Moisés, responsável por liderar o povo de Israel na conquista de Canaã?",
        ("Josué", "Calebe", "Gideão", "Arão"),
        index=None
    )

    q3 = st.radio(
        "3. Na parábola do Semeador, o que representam as sementes que caíram entre os espinhos??",
        ("Pessoas sufocadas pelas preocupações", "Pessoas que desistem na perseguição", "Pessoas que produzem muitos frutos", "Pessoas que não entendem a palavra"),
        index=None
    )

    q4 = st.radio(
        "4. Quem foi o profeta que confrontou o rei Acabe e os profetas de Baal no Monte Carmelo?",
        ("Samuel", "Eliseu", "Isaías", "Elias"),
        index=None
    )

    q5 = st.radio(
        "5. Qual era a profissão de lucas,o auto do terceiro evangelho e do livro de Atos?",
        ("Publicando", "Tendeiro", "Médico", "Pescador"),
        index=None
    )

    q6 = st.radio(
        "6. Qual apóstolo foi escolhido para substituir Judas Iscariotes no grupo dos doze?",
        ("Estêvão", "Barnabé", "Matias", "Paulo"),
        index=None
    )
    q7 =st.radio(
        "7. Quantas pessoas foram salvas na arca de Noé durante o Dilúvio?",
        ("Sete Pessoas", "Oito Pessoas ", "Quatro Pessoas ", "Duas Pessoas "),
        index=None
    )
    q8 = st.radio(
        "8. Em qual cidade os discípulos foram chamados de 'cristãos' pela primeira vez?",
        ("Antioquia", "Jerusarém", "Rama", "Damasco"),
        index=None
    )
    q9 =st.radio(
        "9. Quem escreveu a maior parte dos Salmos contidos na Bíblia?",
        ("Salomão", "Moisés", "Davi", "Asafe"),
        index=None
    )
    q10 = st.radio(
        "10. Quantos livros compõem o Novo Testamento? ",
        ("39 Livros", "66 Livros", " 27 Livros ", "12 Livros "),
        index=None
    )


    # Botão de envio dentro do formulário
    submitted = st.form_submit_button("Ver Resultado 🚀")

# Lógica após o usuário clicar em enviar
if submitted:
    if q1 is None or q2 is None or q3 is None or q4 is None or q5 is None or q6 is None or q7 is None or q8 is None or q9 is None or q10 is None:
        st.warning("⚠️ Por favor, responda a todas as perguntas antes de enviar!")
    else:
        score = 0
        if q1 == "Quarto dia":
            score += 1
        if q2 == "Josué":
            score += 1
        if q3 == "Pessoas sufocadas pelas preocupações":
            score += 1
        if q4 == "Elias":
            score += 1
        if q5 == "Médico":
            score += 1
        if q6 == "Matias":
            score += 1
        if q7 == "Oito Pessoas":
            score += 1
        if q8 == "Antioquia":
            score += 1
        if q9 == "Davi":
            score += 1
        if q10 == "27 Livros":
            score += 1


        st.markdown("---")
        st.subheader(f"Sua pontuação: {score} / 10")

        if score == 10:


            st.balloons()
            st.success("🏆 Perfeito! Você gabaritou o quiz!")
        elif score > 0:
            st.info("👍 Bom trabalho! Mas dá para fazer ainda melhor.")
        else:
            st.error("😅 Não foi dessa vez! Tente novamente.")

