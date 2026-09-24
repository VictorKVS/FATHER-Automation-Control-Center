import type { BehaviorState, SceneAnchor } from "./presenceController";
import { sceneAnchors } from "./AlinaScene";

export type Vec3 = readonly [number, number, number];

export type LocomotionState = {
  anchor: SceneAnchor;
  targetAnchor: SceneAnchor;
  position: Vec3;
  yaw: number;
  behavior: BehaviorState;
  moving: boolean;
};

const avatarPosition = (anchor: SceneAnchor): Vec3 => {
  const [x,,z] = sceneAnchors[anchor];
  return [x,0,z];
};

export const initialLocomotionState = (): LocomotionState => ({
  anchor: "WORK_TABLE",
  targetAnchor: "WORK_TABLE",
  position: avatarPosition("WORK_TABLE"),
  yaw: Math.PI,
  behavior: "IDLE",
  moving: false,
});

export const requestMove = (
  state: LocomotionState,
  targetAnchor: SceneAnchor,
): LocomotionState => ({
  ...state,
  targetAnchor,
  behavior: "WALKING",
  moving: targetAnchor !== state.anchor,
});

export const stepLocomotion = (
  state: LocomotionState,
  deltaSeconds: number,
  speed = 1.35,
): LocomotionState => {
  if (!state.moving) return state;
  const target = avatarPosition(state.targetAnchor);
  const dx = target[0] - state.position[0];
  const dz = target[2] - state.position[2];
  const distance = Math.hypot(dx,dz);
  if (distance < 0.04) {
    return {
      ...state,
      anchor: state.targetAnchor,
      position: target,
      moving: false,
      behavior: state.targetAnchor === "INFORMATION_WALL" ? "PRESENTING" : "IDLE",
      yaw: state.targetAnchor === "INFORMATION_WALL" ? 0 : Math.PI,
    };
  }
  const amount = Math.min(distance,speed*deltaSeconds);
  const position:Vec3=[
    state.position[0]+dx/distance*amount,
    0,
    state.position[2]+dz/distance*amount,
  ];
  return {...state,position,yaw:Math.atan2(dx,dz),behavior:"WALKING"};
};
