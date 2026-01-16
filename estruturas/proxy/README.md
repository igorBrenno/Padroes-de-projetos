# Padrão de Projeto: Proxy

## 📌 Objetivo
O **Proxy** é um padrão de projeto estrutural que permite que você forneça um substituto ou um espaço reservado para outro objeto. Ele controla o acesso ao objeto original, permitindo que você execute tarefas como verificação de segurança, cache ou inicialização preguiçosa.

---

## 🧩 Como funciona?
Imagine um **Cartão de Débito**. O cartão é um **Proxy** para o seu dinheiro vivo. Em vez de carregar notas pesadas ou perigosas (Objeto Real), você usa o cartão (Proxy). O cartão verifica se você tem saldo e se a senha está correta antes de autorizar a transação no banco.

### Tipos Comuns de Proxy:
1.  **Proxy Virtual**: Adia a criação de um objeto pesado até que ele seja realmente necessário (Lazy Loading).
2.  **Proxy de Proteção**: Controla quem tem acesso a determinados métodos do objeto real (Segurança).
3.  **Proxy Remoto**: Representa um objeto que está em um servidor ou local diferente (Rede).
4.  **Proxy de Cache**: Armazena resultados de operações caras para evitar execuções repetitivas.

## ✅ Vantagens
* **Controle**: Permite gerenciar o ciclo de vida do objeto real sem que o cliente saiba.
* **Performance**: Melhora o desempenho através de cache ou carregamento tardio.
* **Segurança**: Introduz uma camada de validação robusta.

## ❌ Desvantagens
* **Complexidade**: Introduz novas classes ao sistema.
* **Latência**: Pode haver um pequeno atraso na resposta devido ao processamento extra dentro do Proxy.