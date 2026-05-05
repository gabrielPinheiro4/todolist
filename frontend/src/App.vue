<script setup lang="ts">
import { computed } from 'vue';

import { RouterView } from 'vue-router'

import { useUserStore } from './stores/user';

import Toast from 'primevue/toast';
import NavbarDesktop from './components/navbar/NavbarDesktop.vue';
import LoginCadForm from './components/modal/LoginCadForm.vue';

const { userLoggedIn } = useUserStore();

const user = computed(() => userLoggedIn());

</script>

<template>

  <Toast position="bottom-center"/>

  <LoginCadForm v-if="!user"/>

  <NavbarDesktop/>

  <main v-if="user">
    <RouterView />
  </main>

</template>

<style scoped>

main {
  padding: 1rem;
}

</style>
