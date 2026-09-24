import type { VRM } from "@pixiv/three-vrm";
import { Euler, Quaternion } from "three";
import type { AnimationIntent } from "./animationIntent";

type BoneName =
  | "leftUpperArm" | "rightUpperArm"
  | "leftLowerArm" | "rightLowerArm"
  | "leftUpperLeg" | "rightUpperLeg"
  | "leftLowerLeg" | "rightLowerLeg";

const setBone = (vrm:VRM,bone:BoneName,x:number,y:number,z:number) => {
  const node=vrm.humanoid?.getNormalizedBoneNode(bone);
  if(!node) return;
  node.quaternion.copy(new Quaternion().setFromEuler(new Euler(x,y,z)));
};

export const applyProceduralPose = (
  vrm:VRM,
  intent:AnimationIntent,
  elapsedSeconds:number,
) => {
  const walk=intent==="WALK_FORWARD";
  const phase=walk ? Math.sin(elapsedSeconds*8) : Math.sin(elapsedSeconds*1.4)*0.04;

  // Neutral relaxed arms remove the rigid T-pose even before external clips exist.
  setBone(vrm,"leftUpperArm",0,0,-1.18 + (walk ? phase*.18 : phase));
  setBone(vrm,"rightUpperArm",0,0,1.18 - (walk ? phase*.18 : phase));
  setBone(vrm,"leftLowerArm",0,0,-0.12);
  setBone(vrm,"rightLowerArm",0,0,0.12);

  // Lightweight in-place gait. Root translation remains owned by locomotionController.
  setBone(vrm,"leftUpperLeg",walk ? phase*.5 : 0,0,0);
  setBone(vrm,"rightUpperLeg",walk ? -phase*.5 : 0,0,0);
  setBone(vrm,"leftLowerLeg",walk ? Math.max(0,-phase)*.55 : 0,0,0);
  setBone(vrm,"rightLowerLeg",walk ? Math.max(0,phase)*.55 : 0,0,0);
};
