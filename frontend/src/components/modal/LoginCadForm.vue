<script setup lang="ts">
import { defineComponent, ref } from 'vue';

import Dialog from 'primevue/dialog';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password';
import Button from 'primevue/button';

defineComponent({
  name: 'LoginCardModal',
});

const showModal = ref(true);

const loginForm = ref(false);

const cadForm = ref({
  name: '',
  password: '',
  email: ''
});

</script>

<template>

  <Dialog
    v-model:visible="showModal"
    modal
    :style="{ width: '70rem' }"
    :breakpoints="{ '1196px': '75vw', '706px': '90vw' }">

    <template #container="{ closeCallback }">

      <div class="flex flex-row justify-between gap-3 items-center">

        <div class="img-wrapper">
          <img src="../../assets/imgs/office_3.jpg" alt="Escritório">
        </div>

        <div :style="{ paddingRight: '3rem' }" class="form-wrapper flex flex-col">

          <div class="flex flex-col">
            <h2 class="title-form">Crie uma conta</h2>
  
            <p>Já possui uma conta? <span @click="loginForm = true" class="span-pointer">Entrar</span></p>
          </div>
  
          <form class="flex flex-col gap-3 mt-3">

            <div class="flex flex-row flex-wrap gap-2">
              <InputText
                class="input-form"
                v-model="cadForm.name"
                name="name"
                type="text"
                placeholder="Nome" />

                <InputText
                  class="input-form"
                  v-model="cadForm.email"
                  name="email"
                  type="email"
                  placeholder="Email" />
            </div>

            <Password
              v-model="cadForm.password"
              :feedback="false"
              placeholder="Senha" />

            <Button label="Criar conta" />
            
          </form>
        </div>
  
      </div>
    </template>

  </Dialog>

</template>

<style scoped>

.img-wrapper {
  padding: 1rem;
  max-width: 510px;
}

.img-wrapper img {
  border-radius: 10px;
  max-width: 100%;
  max-height: 100%;
}

.logo {
  font-size: 2rem;
}

.title-form {
  font-size: 3rem;
  font-weight: bold;
}

.span-pointer {
  cursor: pointer;
  text-decoration: underline;
  color: blue;
}

@media(max-width: 1196px) {

  .img-wrapper {
    width: 300px;
  }

}

@media(max-width: 1166px) {

  .img-wrapper {
    display: none;
  }

  .form-wrapper {
    margin: 0 auto;
    padding: 5rem 2rem;
  }

}

@media(max-width: 706px) {

  .input-form {
    width: 100%;
  }

}

@media(max-width: 544px) {

  .title-form {
    line-height: 50px;
    margin-bottom: 5px;
  }

}

</style>
