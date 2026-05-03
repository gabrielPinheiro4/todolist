<script setup lang="ts">
import { computed, defineComponent, ref } from 'vue';

import User from '@/models/User';

import Dialog from 'primevue/dialog';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password';
import Button from 'primevue/button';

defineComponent({
  name: 'LoginCardModal',
});

const showModal = ref(true);

const loginForm = ref(false);

const h2Title = computed(
  () => loginForm.value ? 'Entre na sua conta' : 'Crie uma conta'
);

const loginOrCad = computed(
  () => loginForm.value ? 'Não possui uma conta?' : 'Já possui uma conta?' 
);

const link = computed(
  () => loginForm.value ? 'Cadastre-se' : 'Entrar'
);

const form = ref({
  name: '',
  password: '',
  email: ''
});

const emptyForm = () => {

  loginForm.value = !loginForm.value;

  Object.keys(form.value).forEach(key => {
    form.value[key as keyof {name: string, password: string, email: string}] = '';
  });

}

const cadUser = () => {

  const user = new User(
    form.value.name, form.value.password, form.value.email
  );

  user.cadUser();

}

</script>

<template>

  <Dialog
    v-model:visible="showModal"
    modal
    pt:mask:class="backdrop-blur-sm"
    :style="{ width: '70rem' }"
    :breakpoints="{ '1196px': '75vw', '706px': '90vw' }">

    <template #container="{ closeCallback }">

      <div class="flex flex-row justify-between gap-3 items-center">

        <div class="img-wrapper">
          <img src="../../assets/imgs/office_3.jpg" alt="Escritório">
        </div>

        <div :style="{ paddingRight: '3rem' }" class="form-wrapper flex flex-col">

          <div class="flex flex-col">
            <h2 class="title-form">{{ h2Title }}</h2>
  
            <p>{{ loginOrCad }} <span @click="emptyForm" class="span-pointer">{{ link }}</span></p>
          </div>
  
          <form class="flex flex-col gap-3 mt-3">

            <div class="flex flex-row flex-wrap gap-2">
              <InputText
                v-if="!loginForm"
                class="input-form"
                v-model="form.name"
                name="name"
                type="text"
                placeholder="Nome" />

                <InputText
                  :style="{ width: loginForm ? '100%' : 'auto' }"
                  class="input-form"
                  v-model="form.email"
                  name="email"
                  type="email"
                  placeholder="Email" />
            </div>

            <Password
              v-model="form.password"
              :feedback="false"
              placeholder="Senha" />

            <Button @click="cadUser" label="Criar conta" />
            
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
    width: 100% !important;
  }

}

@media(max-width: 544px) {

  .title-form {
    line-height: 50px;
    margin-bottom: 5px;
  }

}

</style>
