import api from '@/axios/axios';
import Cookies from 'js-cookie'

import { checkType } from '@/utils/check';
import type { ProjectInterface } from '@/types/env';


export default class Project {

  title: string;
  desc: string;

  constructor(title: string, desc: string) {
    this.title = title;
    this.desc = desc;
  }

  async addProject() {

    try {

      const jwt = Cookies.get('csrf_access_token');

      if (jwt) {

        const res = await api.post('/projects', {
          title: this.title,
          desc: this.desc
        }, {
          headers: { 'X-CSRF-TOKEN': jwt },
          withCredentials: true
        });

        if (typeof res.data === 'string') {
          return res.data;
        }
      }

    } catch(error) {
      throw error;
    }
  }

  static async getProjects(projectID?: string) {

    const jwt = Cookies.get('csrf_access_token');

    if (jwt) {

      const res = await api.get('/projects', {
        headers: { 'X-CSRF-TOKEN': jwt },
        params: { projectID },
        withCredentials: true
      });

      if (!projectID) {

        if (res.data instanceof Array) {

          if(res.data.every(item => checkType<ProjectInterface>(item, 'title'))) {
            return res.data;
          }

        }
      }

      if (checkType<ProjectInterface>(res.data, 'title')) {
        return res.data;
      }
    }

    return null;
  }

  static async delProject(projectName: string) {

    try {

      const jwt = Cookies.get('csrf_access_token');

      if (jwt) {

        const res = await api.delete('/projects', {
          data: { projectName },
          headers: { 'X-CSRF-TOKEN': jwt },
          withCredentials: true
        });

        if (typeof res.data == 'string') {
          return res.data;
        }
      }

    } catch (error) {
      throw error;
    }
  }

  static async editProject(
    projectName: string, newProjectName: string, newDesc: string
  )
  {

    try {

      const jwt = Cookies.get('csrf_access_token');

      if (jwt) {

        const res = await api.patch('/projects',
          { projectName, newProjectName, newDesc },
          { headers: { 'X-CSRF-TOKEN': jwt }, withCredentials: true }
        );

        if (typeof res.data === 'string') return res.data;

      }

    } catch(error) {
      throw error;
    }
  }
}
