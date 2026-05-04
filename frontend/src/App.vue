<script setup lang="ts">
import { computed } from 'vue';

import { RouterLink, RouterView } from 'vue-router'

import { useUserStore } from './stores/user';

import Toast from 'primevue/toast';
import NavbarDesktop from './components/navbar/NavbarDesktop.vue';
import LoginCadForm from './components/modal/LoginCadForm.vue';

const { getUser } = useUserStore();

const user = computed(() => getUser());

console.log(user.value)

</script>

<template>

  <Toast position="bottom-center"/>

  <LoginCadForm v-if="!user"/>

  <NavbarDesktop/>

  <main>
    <RouterView />
  </main>

</template>

<style scoped>

main {
  padding: 1rem;
}

</style>
