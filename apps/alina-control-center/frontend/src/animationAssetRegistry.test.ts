import { describe, expect, it } from "vitest";
import { isVerifiedAnimationAsset, verifiedAnimationMap, type AnimationManifest } from "./animationAssetRegistry";

const sha="a".repeat(64);

describe("ALINA animation asset registry",()=>{
  it("rejects pending assets even if a path exists",()=>{
    expect(isVerifiedAnimationAsset({status:"PENDING_ASSET_REVIEW",path:"/idle.vrma",source:"x",license:"MIT",sha256:sha})).toBe(false);
  });
  it("rejects incomplete provenance",()=>{
    expect(isVerifiedAnimationAsset({status:"LOCAL_VERIFIED",path:"/idle.vrma",source:null,license:"MIT",sha256:sha})).toBe(false);
  });
  it("rejects malformed hashes",()=>{
    expect(isVerifiedAnimationAsset({status:"LOCAL_VERIFIED",path:"/idle.vrma",source:"x",license:"MIT",sha256:"123"})).toBe(false);
  });
  it("publishes only fully verified local clips",()=>{
    const manifest:AnimationManifest={schema_version:"0.1",agent_id:"ALINA",runtime_format:"VRMA",runtime_library:"@pixiv/three-vrm-animation",policy:"LOCAL_ASSET_ONLY_AFTER_LICENSE_REVIEW",assets:{
      IDLE_NEUTRAL:{status:"LOCAL_VERIFIED",path:"/idle.vrma",source:"source",license:"reviewed",sha256:sha},
      WALK_FORWARD:{status:"PENDING_ASSET_REVIEW",path:"/walk.vrma",source:"source",license:"reviewed",sha256:sha},
    }};
    expect(verifiedAnimationMap(manifest)).toEqual({IDLE_NEUTRAL:"/idle.vrma"});
  });
});
