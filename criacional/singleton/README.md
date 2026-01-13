# Singleton Pattern 🔂

## Descrição
O **Singleton** garante que uma classe tenha apenas uma única instância e fornece um ponto de acesso global a ela.

## 🛠 Como funciona?
A classe intercepta a criação de novos objetos. Se uma instância já foi criada anteriormente, ela retorna a referência desse objeto existente em vez de criar um novo.

## ✅ Vantagens
- **Acesso controlado:** Controle estrito sobre como e quando os clientes acessam a instância.
- **Redução de memória:** Evita a criação redundante de objetos pesados.

## ⚠️ Desvantagens
- **Dificuldade em testes unitários:** Como o estado é global, um teste pode interferir no outro.
- **Acoplamento oculto:** Pode esconder dependências ruins no sistema através de um acesso global fácil.