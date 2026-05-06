export interface UserInterface {
  name: string;
  email: string;
  passwd: string;
}

export interface ProjectInterface {
  id: number;
  title: string;
  desc: string;
  date_creation: Date;
}

export interface StatusPriorityInterface {
  id: number;
  title: string;
}
