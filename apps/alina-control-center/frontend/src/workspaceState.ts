import type { AvatarPresence } from "./types";

export const WORKSPACE_STORAGE_KEY = "father.alina.m1.workspace.v1";

export interface PresentationState {
  focus: boolean;
  boardOpen: boolean;
  presence: AvatarPresence;
}

export const defaultPresentationState: PresentationState = {
  focus: false,
  boardOpen: true,
  presence: "COMPACT_3D",
};

export function loadPresentationState(storage: Pick<Storage, "getItem"> = localStorage): PresentationState {
  try {
    const raw = storage.getItem(WORKSPACE_STORAGE_KEY);
    if (!raw) return defaultPresentationState;
    const parsed = JSON.parse(raw) as Partial<PresentationState>;
    const allowed = ["COMPACT_3D","EYES","STATUS","HIDDEN"];
    return {
      focus: typeof parsed.focus === "boolean" ? parsed.focus : false,
      boardOpen: typeof parsed.boardOpen === "boolean" ? parsed.boardOpen : true,
      presence: allowed.includes(String(parsed.presence))
        ? parsed.presence as AvatarPresence
        : "COMPACT_3D",
    };
  } catch {
    return defaultPresentationState;
  }
}

export function savePresentationState(
  state: PresentationState,
  storage: Pick<Storage, "setItem"> = localStorage,
): void {
  storage.setItem(WORKSPACE_STORAGE_KEY, JSON.stringify(state));
}
