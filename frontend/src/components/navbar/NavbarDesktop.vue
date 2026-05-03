<script setup lang="ts">
import { defineComponent } from 'vue';

import Button from 'primevue/button';


defineComponent({
  name: 'NavbarDesktop',
})

</script>

<template>
  <nav class="navbar-desktop flex flex-col items-center gap-4">

    <div class="first flex flex-row">
      <div class="user">
        <span>Nome do usuario</span>
      </div>
    </div>

    <ul class="buttons flex flex-col gap-2">

      <li class="flex flex-row items-center">
        <Button
          class="btn-start"
          severity="primary"
          variant="text"
          type="button"
          label="Adicionar tarefa"
          icon="pi pi-plus" />
      </li>

      <li class="flex flex-row items-center">
        <Button
          class="btn-start"
          severity="secondary"
          variant="text"
          type="button"
          label="Buscar"
          icon="pi pi-search" />
      </li>
    </ul>

  </nav>
</template>

<style scoped>

.navbar-desktop {
  padding: 20px;
  background: #fcfaf8 !important;
  height: 100vh;
  width: 280px;
}

</style>
