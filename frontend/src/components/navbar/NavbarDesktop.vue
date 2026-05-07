<script setup lang="ts">
import { useTaskStore } from '@/stores/task';
import { RouterLink, useRouter } from 'vue-router';
import { isAxiosError } from 'axios';
import { useUserStore } from '@/stores/user';
import { useToast } from 'primevue/usetoast';
import { computed, defineComponent, onBeforeMount, ref, watch } from 'vue';

import Select from 'primevue/select';
import DatePicker from 'primevue/datepicker';
import Popover from 'primevue/popover';
import Message from 'primevue/message';
import InputText from 'primevue/inputtext';
import Dialog from 'primevue/dialog';
import Tree from 'primevue/tree';
import Button from 'primevue/button';

import Project from '@/models/Project';
import Priority from '@/models/Priority';
import Task from '@/models/Task';

import type { ProjectInterface, StatusPriorityInterface, UserInterface } from '@/types/env';

defineComponent({
  name: 'NavbarDesktop',
});

const { push } = useRouter();

const { add } = useToast();

const { updatedValues } = useTaskStore();

const showModalProject = ref(false);

const showEditProjectModal = ref(false);

const showAddTaskModal = ref(false);

const formEditProjectDiferent = ref(false);

const projectSelectedDots = ref<string | null>(null);

const popOver = ref();

const user = ref<UserInterface | null>(null);

const projects = ref<ProjectInterface[] | null>(null);

const priorities = ref<StatusPriorityInterface[] | null>(null);

const projectSelectedComp = computed(() => {

  if (projects.value && projectSelectedDots.value) {

    return projects.value.find(
      item => item.title === projectSelectedDots.value
    );
  }

  return null;
});

const formNewProject = ref({
  title: '',
  desc: ''
});

const formEditProject = ref({
  title: '',
  desc: ''
});

const formNewTask = ref({
  title: '',
  desc: '',
  dateCreation: new Date(),
  prioritySelected: {} as StatusPriorityInterface,
  projectSelected: {} as ProjectInterface,
});

const formNotComplete = computed(
  () => !formNewTask.value.title
  || !formNewTask.value.desc
  || Object.keys(formNewTask.value.projectSelected).length === 0
  || Object.keys(formNewTask.value.prioritySelected).length === 0
);

watch(
  [
    projectSelectedComp,
    () => formEditProject.value.title,
    () => formEditProject.value.desc,
  ],
  (
    [newValueProject, newTitle, newDesc],
    [oldValueProject]

  ) => {

  if (
    !oldValueProject && newValueProject
    || (newValueProject && oldValueProject) && newValueProject?.id !== oldValueProject?.id
  )
  {
    formEditProject.value.title = newValueProject.title;
    formEditProject.value.desc = newValueProject.desc;
  }

  if (newValueProject) {

    if (newTitle && newDesc) {

      if (
        newTitle.toLowerCase().trim() === newValueProject.title.toLowerCase().trim()
        && newDesc.toLowerCase().trim() === newValueProject.desc.toLowerCase().trim()
      )
      {
        formEditProjectDiferent.value = false;
      }
  
      if (
        newTitle.toLowerCase().trim() !== newValueProject.title.toLowerCase().trim()
        || newDesc.toLowerCase().trim() !== newValueProject.desc.toLowerCase().trim()
      )
      {
        formEditProjectDiferent.value = true;
      }
    }

  }

});

const nodeTree = computed(() => [{
  key: '0',
  label: 'Projetos',
  children: projects.value?.map((item, index) => {

    return { key: `0-${index}`, label: item.title, id: item.id }
  })
}]);

const toggle = (event: PointerEvent) => {

  let parentEl: HTMLElement | null = null;

  if (event.target instanceof HTMLSpanElement) {
    parentEl = event.target.parentElement!.parentElement;
  }

  if (event.target instanceof HTMLButtonElement) {
    parentEl = event.target.parentElement
  }

  if (parentEl) {

    if (parentEl.firstChild instanceof HTMLAnchorElement) {

      projectSelectedDots.value = parentEl.firstChild.innerText;
    }

  }

  popOver.value.toggle(event);
}

const addProject = async () => {

  try {

    const project = new Project(
      formNewProject.value.title,
      formNewProject.value.desc
    );

    const res = await project.addProject();

    if (res) {

      add({
        severity: 'success',
        summary: 'Sucesso',
        detail: res,
        life: 4000
      });

      await getData();

      showModalProject.value = false;
    }

  } catch(error) {
    if (isAxiosError(error)) {

      if (error.status === 409) {

        add({
          severity: 'warn',
          summary: 'Atenção',
          detail: error.response?.data.message,
          life: 4000
        });
      }
    }
  }
}

const editProject = async () => {

  const res = await Project.editProject(
    projectSelectedComp.value!.id,
    formEditProject.value.title,
    formEditProject.value.desc
  );

  if (res) {

    add({
      severity: 'success',
      summary: 'Sucesso',
      detail: res,
      life: 4000
    });

    await getData();

    updatedValues(true);

    showEditProjectModal.value = false;
  }
}

const delProject = async () => {

  try {

    if (projectSelectedDots.value) {

      const res = await Project.delProject(projectSelectedDots.value);

      if (res) {

        add({
          severity: 'success',
          summary: 'Sucesso',
          detail: res,
          life: 4000
        });

        await getData();
      }
    }

  } catch (error) {

    if (isAxiosError(error)) {

      if (error.status === 404) {

        add({
          severity: 'error',
          summary: 'Error',
          detail: error,
          life: 4000
        });
      }
    }
  }
}

const addTask = async () => {

  try {

    const newTask = new Task(
      formNewTask.value.title,
      formNewTask.value.desc,
      formNewTask.value.dateCreation,
      formNewTask.value.prioritySelected.id,
      formNewTask.value.projectSelected.id,
    );

    const res = await newTask.addTask();

    if (res) {

      add({
        severity: 'success',
        summary: 'Sucesso',
        detail: res,
        life: 4000
      });

      await getData();

      showAddTaskModal.value = false;

      updatedValues(true);
    }

  } catch (error) {

    if (isAxiosError(error)) {
      add({
        severity: 'error',
        summary: 'Error',
        detail: error,
        life: 4000
      });
    }

  }
}

const getData = async () => {

  const allProjects = await Project.getProjects();

  const allPriorities = await Priority.getPriorities();

  if (allProjects instanceof Array) projects.value = allProjects;

  if (allPriorities) priorities.value = allPriorities;
}

onBeforeMount(async () => {

  const { getUser } = useUserStore();

  const userLogged = await getUser;

  if (userLogged) user.value = userLogged;

  await getData()
});

</script>

<template>

  <Dialog
    v-model:visible="showAddTaskModal"
    position="top"
    :draggable="false"
    :style="{ width: '35rem', padding: '1rem', boxShadow: '0 15px 50px rgba(0,0,0,.35)' }">

    <template #container="{ closeCallback }">
      
      <div class="flex flex-col gap-3">

        <div class="flex flex-col">

          <InputText
            :style="{ paddingBottom: '0', paddingLeft: '0' }"
            class="new-task-input task-bold"
            type="text"
            placeholder="Ex: Mandar formulário na quarta-feira"
            v-model="formNewTask.title" />

          <InputText
            :style="{paddingLeft: '0'}"
            size="small"
            class="new-task-input"
            type="text"
            placeholder="Descrição"
            v-model="formNewTask.desc" />

        </div>

        <div class="flex flex-row flex-wrap gap-3">

          <div class="flex flex-col gap-1 items-end">

            <DatePicker
              :style="{width: '8rem'}"
              v-model="formNewTask.dateCreation"
              dateFormat="dd/mm/yy"
              size="small"
              showIcon
              fluid
              iconDisplay="input"
              inputId="icondisplay" />
          </div>

          <Select
            v-if="priorities"
            v-model="formNewTask.prioritySelected"
            :options="priorities"
            size="small"
            optionLabel="title"
            placeholder="Prioridade" />

        </div>

        <div class="flex flex-row flex-wrap justify-between">

          <Select
            :style="{border: 'none', boxShadow: 'none'}"
            v-if="projects"
            v-model="formNewTask.projectSelected"
            :options="projects"
            size="small"
            optionLabel="title"
            placeholder="Projeto" />

          <div class="flex flex-row flex-wrap gap-2">

            <Button
              size="small"
              type="button"
              label="Cancelar"
              severity="secondary"
              @click="showAddTaskModal = false" />

            <Button
              size="small"
              type="button"
              label="Adicionar tarefa"
              :disabled="formNotComplete"
              @click="addTask" />
          </div>

        </div>

      </div>
    </template>

  </Dialog>

  <Dialog
    modal
    v-model:visible="showModalProject"
    header="Adicionar projeto"
    :draggable="false"
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
        @click="addProject" />
    </div>

  </Dialog>

  <Dialog
    modal
    v-model:visible="showEditProjectModal"
    header="Editar projeto"
    :draggable="false"
    :style="{ width: '25rem' }">

    <span class="text-surface-500 dark:text-surface-400 block mb-8">
      Modifique os campos a seguir para editar um projeto
    </span>

    <div class="flex flex-col gap-4">

      <div class="flex flex-col gap-1">

        <InputText
          v-model="formEditProject.title"
          maxlength="60"
          size="small"
          placeholder="Título"
          class="flex-auto" />

        <Message
          size="small"
          severity="secondary"
          variant="simple">
          {{ formEditProject.title!.length }}/60
        </Message>

      </div>

      <div class="flex flex-col gap-1">

        <InputText
          v-model="formEditProject.desc"
          size="small"
          maxlength="80"
          placeholder="Descrição"
          class="flex-auto" />

          <Message
            size="small"
            severity="secondary"
            variant="simple">
            {{ formEditProject.desc!.length }}/80
        </Message>
      </div>

    </div>

    <div class="flex justify-end gap-2">
      <Button
        size="small"
        type="button"
        label="Cancelar"
        severity="secondary"
        @click="showEditProjectModal = false" />

      <Button
        size="small"
        type="button"
        label="Editar"
        :disabled="!formEditProjectDiferent || (!formEditProject.title || !formEditProject.desc)"
        @click="editProject"/>
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
          @click="showAddTaskModal = true"
          size="small"
          class="btn-start"
          severity="primary"
          variant="text"
          type="button"
          label="Adicionar tarefa"
          icon="pi pi-plus" />
      </li>

      <li>
        <Button
          @click="push({ name: 'home' })"
          size="small"
          class="btn-start"
          severity="secondary"
          variant="text"
          icon="pi pi-home"
          label="Entrada"
          type="button" />
      </li>

    </ul>

    <div class="flex flex-row justify-between items-start">

      <Tree :value="nodeTree" class="w-full tree-projects">

        <template #default="slotProps">
          <div class="flex flex-row items-center justify-between">

            <RouterLink
              v-if="slotProps.node.label !== 'Projetos'"
              class="project-link"
              :to="`/project/${slotProps.node.id}`">
              {{ slotProps.node.label }}
            </RouterLink>

            <p v-else>{{ slotProps.node.label }}</p>

            <Button
              v-if="slotProps.node.label != 'Projetos'"
              @click="toggle"
              size="small"
              icon="pi pi-ellipsis-h"
              variant="text"
              severity="secondary" />
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

    <Popover ref="popOver">

      <div class="flex flex-col gap-2">
        <Button
          @click="showEditProjectModal = true"
          size="small"
          icon="pi pi-pencil"
          variant="text"
          label="Editar"
          severity="secondary" />

          <Button
            @click="delProject"
            size="small"
            icon="pi pi-trash"
            variant="text"
            label="Deletar"
            severity="danger" />
      </div>

    </Popover>

  </nav>
</template>

<style scoped>

.navbar-desktop {
  padding: 20px;
  background: #fcfaf8 !important;
  height: 100vh;
  width: 300px;
  position: fixed;
  z-index: 1;
}

.icon-user {
  background: orange;
  color: #fff;
  padding: 2px 10px;
  border-radius: 100%;
  font-weight: bold;
}

</style>
