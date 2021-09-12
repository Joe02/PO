from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, sexo, parts):
        self.nome = nome
        self.sexo = sexo
        self.parts = parts

    def list_parts(self):
        print(f"Partes do corpo presentes: {', '.join(self.parts)}", end="")
        print(f'\nNome da pessoa = {self.nome}, do genero = {self.sexo}')


class Homem(Pessoa):
    def __init__(self, nome, parts):
        super().__init__(nome, 'Homem', parts)


class Mulher(Pessoa):
    def __init__(self, nome, parts):
        super().__init__(nome, 'Mulher', parts)


class FactoryPessoa:
    @staticmethod
    def getPessoa(nome, sexo, *args, **kwargs):
        if sexo == 'Homem':
            return Homem(nome, *args, **kwargs)
        elif sexo == 'Mulher':
            return Mulher(nome, *args, **kwargs)
        else:
            raise ValueError("Not supported or something")


class Builder(ABC):
    @property
    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def produce_part_a(self):
        pass

    @abstractmethod
    def produce_part_b(self):
        pass

    @abstractmethod
    def produce_part_c(self):
        pass


class ConcreteBuilder(Builder):
    def __init__(self):
        self.parts = []

    def build(self, nome, sexo):
        pessoa = FactoryPessoa.getPessoa(nome, sexo, self.parts)
        self.parts = []
        return pessoa

    def produce_part_a(self):
        self.parts.append("Cabeca")
        return self

    def produce_part_b(self):
        self.parts.append("Pernas")
        return self

    def produce_part_c(self):
        self.parts.append("Bracos")
        return self


if __name__ == "__main__":

    builder = ConcreteBuilder()

    print("Corpo so com a cabeca: ")
    pessoa1 = builder.produce_part_a().build('José', 'Homem')
    pessoa1.list_parts()

    print("\n")

    print("Corpo com a cabeca e pernas: ")
    pessoa2 = builder.produce_part_a().produce_part_b().build('Maurício', 'Homem')
    pessoa2.list_parts()

    print("\n")

    print("Corpo completo: ")
    pessoa3 = builder.produce_part_a().produce_part_b().produce_part_c().build('Giovanna', 'Mulher')
    pessoa3.list_parts()

    print("\n")