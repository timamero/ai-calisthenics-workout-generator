import { create } from 'zustand';

interface SampleUseStoreState {
  exercise: string;
  addExercise: (name: string) => void;
}

export const useStore = create<SampleUseStoreState>((set) => ({
  exercise: '',
  addExercise: (name) => set({ exercise: name }),
}));
