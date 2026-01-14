# Adapter Pattern 🔌

## Descrição
O **Adapter** é um padrão estrutural que atua como um intermediário entre duas interfaces incompatíveis. Ele permite que classes trabalhem juntas sem que seja necessário modificar o código-fonte original de nenhuma delas.

## 🧱 Componentes
1.  **Target (Alvo):** A interface domínio-específica que o código cliente utiliza.
2.  **Client (Cliente):** Colabora com objetos em conformidade com a interface Alvo.
3.  **Adaptee (Adaptado):** A interface que precisa de adaptação (geralmente uma biblioteca externa).
4.  **Adapter (Adaptador):** Adapta a interface do *Adaptee* para a interface *Target*.

## ✅ Vantagens
- **Princípio da Responsabilidade Única:** Você separa a conversão de interface da lógica de negócio.
- **Princípio do Aberto/Fechado:** Você pode introduzir novos adaptadores sem quebrar o código cliente existente.
- **Reutilização:** Permite o uso de classes legadas ou de terceiros que não seguem seus padrões.

## ⚠️ Desvantagens
- **Complexidade:** Introduz novas classes e interfaces, o que pode ser exagerado se uma mudança simples no código original for possível.

---