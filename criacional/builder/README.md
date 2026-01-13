# Builder Pattern 👷‍♂️

## Descrição
O **Builder** é um padrão de projeto criacional que permite construir objetos complexos passo a passo. O padrão permite produzir diferentes tipos e representações de um objeto usando o mesmo código de construção.

## 🧱 Componentes
1.  **Builder**: Interface que define as etapas de construção comuns a todos os tipos de construtores.
2.  **Concrete Builder**: Fornece implementações específicas das etapas de construção.
3.  **Product**: O objeto complexo resultante.
4.  **Director**: Classe opcional que define a ordem na qual as etapas de construção devem ser executadas.

## ✅ Vantagens
- **Construção Passo a Passo**: Você pode adiar etapas de construção ou executá-las recursivamente.
- **Reutilização**: Use o mesmo código de construção para criar produtos diferentes.
- **Isolamento**: Separa o código de construção complexo da lógica de negócio do produto.

## ⚠️ Desvantagens
- **Complexidade**: A complexidade geral do código aumenta, pois o padrão exige a criação de várias classes novas.
- **Acoplamento**: O cliente precisa estar vinculado a uma classe de builder específica.

---