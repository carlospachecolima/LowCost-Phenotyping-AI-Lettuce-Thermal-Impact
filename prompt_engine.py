# prompt_engine.py

class PromptEngineering:
    """
    Define a metodologia de Prompt Chaining para análise visual de estresse térmico em alface.
    Isso encapsula a autoria intelectual e os critérios técnicos da equipe de pesquisa.
    """
    
    def __init__(self, caminho_foto):
        self.caminho_foto = caminho_foto
        
        # ----------------------------------------------------------------------
        # PROMPT 1: DEFINIÇÃO DA PERSONA E EXPERTISE (Baseado no conhecimento dos autores)
        # ----------------------------------------------------------------------
        self.P1_PERSONA = (
            "Assuma a persona de um Engenheiro Agrônomo com PhD em Fisiologia Vegetal e "
            "com mais de 15 anos de experiência em investigação de estresse térmico e desordens "
            "fisiológicas em alface (Lactuca sativa) sob ambientes tropicais. Você é um especialista "
            "em avaliar a resposta de plantas a biofertilizantes e fertilizantes minerais, "
            "com foco em balanço de nutrientes e termotolerância."
        )

        # ----------------------------------------------------------------------
        # PROMPT 2: OBSERVAÇÃO DE ATRIBUTOS (Foco na detecção que aumenta a capacidade humana)
        # ----------------------------------------------------------------------
        self.P2_ATRIBUTOS = (
            f"As fotos anexadas ('{self.caminho_foto}') mostram plantas de alface sob condições de estresse. "
            "Em cada par, a planta da esquerda recebeu biofertilizante e a da direita, mineral. "
            "Observe e compare os seguintes atributos: "
            "1. Intensidade e uniformidade da cor da folha (verde profundo vs. clorose); "
            "2. Turgor e estado de hidratação do tecido (murcha, perda de rigidez) — (Crucial para a detecção de desidratação); "
            "3. Morfologia e arquitetura da copa (deformação, enrolamento); "
            "4. Vigor geral e distribuição de biomassa; "
            "5. Indicadores de estresse e desordens fisiológicas visíveis."
        )

        # ----------------------------------------------------------------------
        # PROMPT 3: CLASSIFICAÇÃO TÉCNICA (Critérios usados na pesquisa primária)
        # ----------------------------------------------------------------------
        self.P3_CLASSIFICACAO = (
            "Identifique e descreva todas as desordens fisiológicas visíveis, classificando-as pelas categorias: "
            "• Leaf edge burn (tipburn): Necrose nas bordas (cálcio ou estresse térmico); "
            "• Clorose: Amarelecimento (degradação da clorofila ou desequilíbrio de N); "
            "• Necrose: Áreas marrons/escuras (dano celular irreversível); "
            "• Wilting ou Desidratação: Perda de turgidez; "
            "• Bolting ou Elongação do Caule: Crescimento reprodutivo prematuro. "
            "Para cada sintoma, indique o tratamento mais afetado e forneça uma breve interpretação fisiológica da causa subjacente."
        )

        # ----------------------------------------------------------------------
        # PROMPT 4: RANKING DE PERFORMANCE (Escala científica para avaliação)
        # ----------------------------------------------------------------------
        self.P4_RANKING = (
            "Compare os pares (biofertilizante vs. mineral) e atribua um ranking de termotolerância (1 a 5): "
            "5 = Excelente (vigorooso, sintomas mínimos); 4 = Bom (clorose ou murcha leve); 3 = Moderado (tipburn ou necrose localizada); "
            "2 = Fraco (colapso parcial); 1 = Estresse Severo (necrose generalizada). "
            "Gere um ranking final integrado, indicando qual fonte de fertilização conferiu maior termotolerância geral."
        )

        # ----------------------------------------------------------------------
        # PROMPT 5: INTERPRETAÇÃO E CONCLUSÃO (Ligando a análise à hipótese do artigo)
        # ----------------------------------------------------------------------
        self.P5_CONCLUSAO = (
            "Resuma a interpretação fisiológica abordando: 1. Qual tratamento manteve maior integridade de clorofila/hidratação; "
            "2. Desordens específicas predominantes; 3. Como o biofertilizante pode ter mitigado o estresse (ex: ajuste osmótico, hormônios); "
            "4. Se o padrão observado apoia a hipótese de que biofertilizantes melhoram a termotolerância da alface."
        )

    def gerar_prompt_encadeado(self):
        """
        Combina todos os prompts em uma sequência lógica (Chain-of-Thought) que a IA executará.
        Esta é a automatização do seu método.
        """
        return f"{self.P1_PERSONA}\n\n[TAREFA 1 - OBSERVAÇÃO]\n{self.P2_ATRIBUTOS}\n\n[TAREFA 2 - CLASSIFICAÇÃO]\n{self.P3_CLASSIFICACAO}\n\n[TAREFA 3 - RANKING]\n{self.P4_RANKING}\n\n[TAREFA 4 - INTERPRETAÇÃO FINAL]\n{self.P5_CONCLUSAO}"

# --------------------------------------------------------------------------------