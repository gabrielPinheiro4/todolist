<script setup lang="ts">
import { useUserStore } from '@/stores/user';
import { computed, defineComponent, onBeforeMount, ref } from 'vue';

import Popover from 'primevue/popover';
import Message from 'primevue/message';
import InputText from 'primevue/inputtext';
import Dialog from 'primevue/dialog';
import Tree from 'primevue/tree';
import Button from 'primevue/button';

import type { ProjectInterface, UserInterface } from '@/types/env';
import Project from '@/models/Project';

defineComponent({
  name: 'NavbarDesktop',
});

const showModalProject = ref(false);

const popOver = ref();

const selectedKey = ref();

const user = ref<UserInterface | null>(null);

const projects = ref<ProjectInterface[] | null>(null);

const formNewProject = ref({
  title: '',
  desc: ''
});

const nodeTree = computed(() => [{
  key: '0',
  label: 'Projetos',
  children: projects.value?.map((item, index) => {

    return { key: `0-${index}`, label: item.title }
  })
}]);

const toggle = (event: event) => {
  popOver.value.toggle(event);
}

const addProject = async () => {

  const project = new Project(
    formNewProject.value.title,
    formNewProject.value.desc
  );

  await project.addProject();
}

onBeforeMount(async () => {

  const { getUser } = useUserStore();

  const allProjects = await Project.getAllProjects();

  const userLogged = await getUser;

  if (userLogged) user.value = userLogged;

  if (allProjects) projects.value = allProjects;

});

</script>

<template>

  <Dialog
    modal
    v-model:visible="showModalProject"
    header="Adicionar projeto"
    :style="{ width: '25rem' }">

    <span class="text-surface-500 dark:text-surface-400 block mb-8">
      Preencha os campos a seguir para adicionar um projeto
    </span>

    <div class="flex flex-col gap-4">

      <div class="flex flex-col gap-1">

        <InputText
          v-model="formNewProject.title"
          maxlength="60"
          size="small"
          placeholder="Título"
          class="flex-auto" />

        <Message
          size="small"
          severity="secondary"
          variant="simple">
          {{ formNewProject.title.length }}/60
        </Message>

      </div>

      <div class="flex flex-col gap-1">

        <InputText
          v-model="formNewProject.desc"
          size="small"
          maxlength="80"
          placeholder="Descrição"
          class="flex-auto" />

          <Message
            size="small"
            severity="secondary"
            variant="simple">
            {{ formNewProject.desc.length }}/80
        </Message>
      </div>

    </div>

    <div class="flex justify-end gap-2">
      <Button
        size="small"
        type="button"
        label="Cancelar"
        severity="secondary"
        @click="showModalProject = false" />

      <Button
        size="small"
        type="button"
        label="Adicionar"
        :disabled="!formNewProject.title || !formNewProject.desc"
        @click="addProject"/>
    </div>

  </Dialog>

  <nav class="navbar-desktop flex flex-col gap-4">

    <div class="first flex flex-row">
      <div class="user flex items-center flex-row gap-2">
        <p class="icon-user">{{ user?.name[0]?.toUpperCase() }}</p>
        <p>{{ user?.name }}</p>
      </div>
    </div>

    <ul class="buttons flex flex-col gap-2">

      <li class="flex flex-row items-center">
        <Button
          size="small"
          class="btn-start"
          severity="primary"
          variant="text"
          type="button"
          label="Adicionar tarefa"
          icon="pi pi-plus" />
      </li>

      <li class="flex flex-row items-center">
        <Button
          size="small"
          class="btn-start"
          severity="secondary"
          variant="text"
          type="button"
          label="Buscar"
          icon="pi pi-search" />
      </li>
    </ul>

    <div class="flex flex-row justify-between items-start">

      <Tree
        v-model:selectionKeys="selectedKey"
        :value="nodeTree"
        selectionMode="single"
        class="w-full md:w-[30rem] tree-projects">

        <template #default="slotProps">
          <div class="flex flex-row items-center justify-between">
            <p>{{ slotProps.node.label }}</p>

            <Button
              v-if="slotProps.node.label != 'Projetos'"
              @click="toggle"
              size="small"
              icon="pi pi-ellipsis-h"
              variant="text"
              severity="secondary" />

            <Popover ref="popOver">

              <div class="flex flex-col gap-2">
                <Button
                  size="small"
                  icon="pi pi-pencil"
                  variant="text"
                  label="Editar"
                  severity="secondary" />

                  <Button
                    size="small"
                    icon="pi pi-trash"
                    variant="text"
                    label="Deletar"
                    severity="danger" />
              </div>

            </Popover>
          </div>
        </template>

      </Tree>

      <Button
        size="small"
        @click="showModalProject = true"
        severity="contrast"
        icon="pi pi-plus"
        variant="text" />
    </div>

  </nav>
</template>

<style scoped>

.navbar-desktop {
  padding: 20px;
  background: #fcfaf8 !important;
  height: 100vh;
  width: 280px;
}

.icon-user {
  background: orange;
  color: #fff;
  padding: 2px 10px;
  border-radius: 100%;
  font-weight: bold;
}

</style>
