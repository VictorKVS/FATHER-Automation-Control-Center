import type { HumanAgentProfile } from "./humanAgentProfile";
import type { BehaviorState, SceneAnchor } from "./presenceController";

export type AvatarRendererCapabilities = {
  vrm: boolean;
  glb: boolean;
  locomotion: boolean;
  gaze: boolean;
  lipSync: boolean;
};

export interface AvatarRendererAdapter {
  readonly id: string;
  readonly capabilities: AvatarRendererCapabilities;
  canRender(profile: HumanAgentProfile): boolean;
  load(profile: HumanAgentProfile): Promise<void>;
  moveTo(anchor: SceneAnchor): Promise<void>;
  setBehavior(state: BehaviorState): Promise<void>;
  dispose(): Promise<void>;
}

export const isAvatarAssetPromotable = (profile: HumanAgentProfile) =>
  profile.avatar.licenseStatus === "APPROVED" &&
  profile.avatar.provenanceRef.trim().length > 0;

export class PlaceholderAvatarRendererAdapter implements AvatarRendererAdapter {
  readonly id = "placeholder-avatar-renderer-v01";
  readonly capabilities: AvatarRendererCapabilities = {
    vrm: false,
    glb: false,
    locomotion: false,
    gaze: false,
    lipSync: false,
  };

  private loadedAgentId: string | null = null;

  canRender(profile: HumanAgentProfile) {
    return profile.id.length > 0 && profile.avatar.licenseStatus !== "REJECTED";
  }

  async load(profile: HumanAgentProfile) {
    if (!this.canRender(profile)) throw new Error("Avatar profile is not renderable");
    this.loadedAgentId = profile.id;
  }

  async moveTo(_anchor: SceneAnchor) {
    if (!this.loadedAgentId) throw new Error("Avatar is not loaded");
  }

  async setBehavior(_state: BehaviorState) {
    if (!this.loadedAgentId) throw new Error("Avatar is not loaded");
  }

  async dispose() {
    this.loadedAgentId = null;
  }
}
