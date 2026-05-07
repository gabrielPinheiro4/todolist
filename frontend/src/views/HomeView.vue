<script setup lang="ts">

</script>

<template>
  <div class="home">
    <h1 class="font-bold titulo">Bem vindo ao <span>ToDo</span>List</h1>

    <div class="flex flex-col gap-3 mt-2">
      <p>
        Com nosso ToDo List, você pode criar,
        organizar e acompanhar suas atividades de maneira prática,
        mantendo o foco no que realmente importa.
      </p>

      <p class="help">Segue abaixo o passo a passo de como criar uma tarefa</p>
    </div>

    <div class="steps flex flex-col gap-3">

      <div class="flex flex-col gap-2">
        <h3>1° Criar um projeto</h3>

        <p>
          Para criar um projeto basta clicar no ícone de "+" que está na sua navbar.
        </p>
      </div>

      <div class="flex flex-col gap-2">
        <h3>2° Criar uma tarefa</h3>

        <p>
          Para criar uma tarefa é preciso clicar no botão "Adicionar tarefa" que
          está na sua navbar e vincular sua nova tarefa à um projeto existente.
        </p>
      </div>

    </div>
  </div>
</template>

<style scoped>

.titulo {
  font-size: 1.7rem;
}

.steps {
  margin-top: 2rem;
}

p {
  width: 30rem;
}

span, h3, .help {
  color: #f97316;
}

</style>
