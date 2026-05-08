<script setup lang="ts">

import { computed, onMounted } from 'vue';
import { RouterView } from 'vue-router'
import { useScreenStore } from './stores/screen';
import { useUserStore } from './stores/user';

import Toast from 'primevue/toast';
import NavbarDesktop from './components/navbar/NavbarDesktop.vue';
import LoginCadForm from './components/modal/LoginCadForm.vue';

const { userLoggedIn } = useUserStore();

const user = computed(() => userLoggedIn());

const { updateScreenWidth } = useScreenStore();

onMounted(() => {
  window.addEventListener('resize', updateScreenWidth);
});

</script>

<template>

  <Toast position="bottom-center"/>

  <LoginCadForm v-if="!user"/>

  <div class="nav-main flex flex-row">

    <NavbarDesktop class="navbar" />

    <main v-if="user">
      <RouterView />
    </main>
  </div>

</template>

<style scoped>

main {
  margin-top: 5rem;
  margin-left: 40rem;
  width: 100%;
}

.navbar {
  position: fixed;
}

.nav-main {
  overflow-x: hidden;
}

@media (max-width: 1480px) {
  main {
    margin-left: 30rem;
  }
}

@media (max-width: 1138px) {
  main {
    margin-left: 25rem;
  }
}

@media (max-width: 1100px) {

  .nav-main {
    padding: 1.5rem;
    flex-direction: column;
  }

  main {
    width: auto;
    max-width: 100%;
    align-self: center;
    margin-left: 0;
  }
}

@media (max-width: 520px) {
  main {
    align-self: self-start;
  }
}


</style>
