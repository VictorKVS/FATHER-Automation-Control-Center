import { describe, expect, it } from "vitest";
import { PlaceholderAvatarRendererAdapter, isAvatarAssetPromotable } from "./avatarRendererAdapter";
import { alinaHumanAgentProfile, type HumanAgentProfile } from "./humanAgentProfile";

describe("Human Agent Studio P2 contracts", () => {
  it("HA-P2-01 keeps ALINA professional identity separate from avatar asset", () => {
    expect(alinaHumanAgentProfile.id).toBe("ALINA-001");
    expect(alinaHumanAgentProfile.professionalIdentityRef).toContain("alina-analyst");
    expect(alinaHumanAgentProfile.avatar.id).not.toBe(alinaHumanAgentProfile.professionalIdentityRef);
  });

  it("HA-P2-02 temporary avatar is usable for the polygon but not promotable", () => {
    const adapter = new PlaceholderAvatarRendererAdapter();
    expect(adapter.canRender(alinaHumanAgentProfile)).toBe(true);
    expect(isAvatarAssetPromotable(alinaHumanAgentProfile)).toBe(false);
  });

  it("HA-P2-03 approved asset requires provenance", () => {
    const candidate: HumanAgentProfile = {
      ...alinaHumanAgentProfile,
      avatar: { ...alinaHumanAgentProfile.avatar, licenseStatus: "APPROVED", provenanceRef: "" },
    };
    expect(isAvatarAssetPromotable(candidate)).toBe(false);
  });

  it("HA-P2-04 renderer lifecycle does not mutate professional identity", async () => {
    const adapter = new PlaceholderAvatarRendererAdapter();
    const before = alinaHumanAgentProfile.professionalIdentityRef;
    await adapter.load(alinaHumanAgentProfile);
    await adapter.setBehavior("THINKING");
    await adapter.moveTo("INFORMATION_WALL");
    await adapter.dispose();
    expect(alinaHumanAgentProfile.professionalIdentityRef).toBe(before);
  });
});
