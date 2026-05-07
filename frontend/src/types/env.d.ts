export interface UserInterface {
  name: string;
  email: string;
  passwd: string;
}

export interface ProjectInterface {
  id: number;
  title: string;
  desc: string;
  dateCreation: string;
  tasks: TaskInterface[];
}

export interface TaskInterface extends ProjectInterface {
  dateExpiration: string;
  priority: StatusPriorityInterface;
  status: StatusPriorityInterface;
}

export interface StatusPriorityInterface {
  id: number;
  title: string;
}
