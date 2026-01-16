# Bridge

## Descrição
O **Bridge** é um padrão de projeto estrutural que foca em separar a abstração (lógica de alto nível) da sua implementação (lógica de plataforma ou técnica). Em vez de uma classe herdar múltiplas responsabilidades, ela utiliza a composição para que ambas as partes possam evoluir de forma independente.

## 🧱 Componentes
1.  **Abstraction (Abstração):** Define a interface de controle que o cliente usa. Mantém uma referência para o Implementador.
2.  **Refined Abstraction (Abstração Refinada):** Estende a interface base, adicionando variantes da lógica de negócio.
3.  **Implementor (Implementador):** Interface comum para todas as classes de implementação técnica.
4.  **Concrete Implementors (Implementadores Concretos):** O código específico que realiza a tarefa real (ex: drivers, APIs, sistemas operacionais).