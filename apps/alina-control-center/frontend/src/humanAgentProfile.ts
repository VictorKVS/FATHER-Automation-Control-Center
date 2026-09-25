import type { BehaviorState, PresenceMode, SceneAnchor } from "./presenceController";

export type HumanAgentAssetRef = {
  id: string;
  kind: "AVATAR";
  uri: string;
  format: "VRM" | "GLB";
  licenseStatus: "TEST_ONLY" | "APPROVED" | "REJECTED" | "UNKNOWN";
  provenanceRef: string;
};

export type HumanAgentProfile = {
  id: string;
  version: string;
  displayName: string;
  professionalIdentityRef: string;
  avatar: HumanAgentAssetRef;
  presentation: {
    presenceMode: PresenceMode;
    behavior: BehaviorState;
    anchor: SceneAnchor;
  };
};

export const alinaHumanAgentProfile: HumanAgentProfile = {
  id: "ALINA-001",
  version: "0.1.0",
  displayName: "ALINA",
  professionalIdentityRef: "father://specialists/alina-analyst",
  avatar: {
    id: "ALINA-TEMP-SEED-SAN",
    kind: "AVATAR",
    uri: "/assets/agents/alina/Seed-san.vrm",
    format: "VRM",
    licenseStatus: "TEST_ONLY",
    provenanceRef: "father://provenance/alina/seed-san-vrm",
  },
  presentation: {
    presenceMode: "FULL_BODY",
    behavior: "IDLE",
    anchor: "WORK_TABLE",
  },
};
