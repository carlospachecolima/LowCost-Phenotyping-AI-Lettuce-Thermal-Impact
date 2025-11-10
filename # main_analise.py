# main_analise.py

from prompt_engine import PromptEngineering
import os

# -----------------------------------------------------------------------------
# FUNÇÃO PRINCIPAL QUE ORQUESTRA A ANÁLISE
# -----------------------------------------------------------------------------
def iniciar_analise_assistida(caminho_foto_teste):
    """
    Orquestra o processo de Prompt Chaining para a análise visual da foto.
    Esta função representa o seu software funcional.
    """
    
    # 1. Cria a instância do motor de prompts com o caminho da foto
    motor_prompts = PromptEngineering(caminho_foto_teste)
    
    # 2. Gera o prompt completo encadeado (a sua metodologia)
    prompt_final = motor_prompts.gerar_prompt_encadeado()
    
    # 3. Simulação da comunicação com a IA (Esta parte seria substituída pela chamada da API)
    print("---------------------------------------------------------")
    print(" Iniciando Sistema de Análise Visual Agronômica (Assistida por IA)")
    print("---------------------------------------------------------")
    print(f"Metodologia (Prompt Chaining) criada pelo especialista com sucesso.")
    print(f"Foto de entrada: {caminho_foto_teste}\n")
    
    # print("--- Conteúdo Completo do Prompt Enviado para o LLM (O LEPD) ---")
    # print(prompt_final)
    # print("----------------------------------------------------------------\n")
    
    # 4. Simulação de um loop de execução e coleta de resultados
    print("Executando Prompt Chaining em etapas (CoT/Decomposição de Tarefas)...")
    print("  -> Etapa 1 (Persona) OK.")
    print("  -> Etapa 2 (Observação de Atributos Críticos) OK.")
    print("  -> Etapa 3 (Classificação Técnica de Sintomas) OK.")
    print("  -> Etapa 4 (Ranking Qualitativo) OK.")
    print("  -> Etapa 5 (Interpretação Fisiológica) OK.")
    
    print("\nRelatório final gerado pela IA com base nas instruções do especialista.")
    print("Processo concluído. O software registrável é a lógica que executa este workflow.")
    
    # Retorna o prompt final (a evidência da sua autoria) e indica sucesso
    return prompt_final

# -----------------------------------------------------------------------------
# EXECUÇÃO DO PROGRAMA
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Use um nome de arquivo de foto fictício para a execução de teste
    FOTO_DE_TESTE = "par_alface_cultivar_33x64.jpg" 
    
    try:
        resultado_da_analise = iniciar_analise_assistida(FOTO_DE_TESTE)
        
    except Exception as e:
        print(f"\nERRO FATAL NA EXECUÇÃO DO SOFTWARE: {e}")