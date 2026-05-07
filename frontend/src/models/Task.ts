import api from "@/axios/axios";
import Cookies from "js-cookie";


export default class Task {

  title: string;
  desc: string;
  dateCreation: Date;
  priorityId: number;
  projectId: number;
  
  constructor (
    title: string,
    desc: string,
    dateCreation: Date,
    priorityId: number,
    projectId: number
  )
  {
    this.title = title;
    this.desc = desc;
    this.dateCreation = dateCreation;
    this.priorityId = priorityId;
    this.projectId =  projectId;

  }

  async addTask () {

    try {

      const jwt = Cookies.get('csrf_access_token');

      if (jwt) {

        const day = (
          this.dateCreation.getDate() <= 9
          ? `0${this.dateCreation.getDate()}`
          : this.dateCreation.getDate()
        );

        const month = (
          this.dateCreation.getMonth() + 1 <= 9
          ? `0${this.dateCreation.getMonth() + 1}`
          : this.dateCreation.getMonth() + 1
        );

        const dateF = (`${this.dateCreation.getFullYear()}-${month}-${day}`)

        const res = await api.post('/tasks',
          {
            title: this.title,
            desc: this.desc,
            dateCreation: dateF,
            priorityId: this.priorityId,
            projectId: this.projectId
          },
          {headers:{ 'X-CSRF-TOKEN': jwt }, withCredentials: true}
        )

        if (typeof res.data === 'string') {
          return res.data;
        }

      }

      return null;

    } catch (error) {

    }
  }

  static async editTask (
    taskId: number,
    title: string,
    desc: string,
    priorityId: number,
    statusId: number,
    dateExpiration: Date
  )
  {

    const jwt = Cookies.get('csrf_access_token');

    if (jwt) {

      const day = (
        dateExpiration.getDate() <= 9
        ? `0${dateExpiration.getDate()}`
        : dateExpiration.getDate()
      );

      const month = (
        dateExpiration.getMonth() + 1 <= 9
        ? `0${dateExpiration.getMonth() + 1}`
        : dateExpiration.getMonth() + 1
      );

      const dateF = (`${dateExpiration.getFullYear()}-${month}-${day}`)

      const res = await api.patch('/tasks', 
        { taskId, title, desc, priorityId, statusId, dateExpiration: dateF },
        { headers:{ 'X-CSRF-TOKEN': jwt }, withCredentials: true }
      )

      if (typeof res.data === 'string') {
        return res.data;
      }
    }

  }

  static async delTask(taskId: number) {

    try {

      const jwt = Cookies.get('csrf_access_token');

      if (jwt) {

        const res = await api.delete('/tasks',{
          data: { taskId },
          headers:{ 'X-CSRF-TOKEN': jwt },
          withCredentials: true
        });

        if (typeof res.data === 'string') {
          return res.data;
        }
      }

    } catch (error) {
      throw error;
    }
  }
}
