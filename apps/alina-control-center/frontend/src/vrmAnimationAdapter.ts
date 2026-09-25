import { AnimationMixer, type AnimationAction } from "three";
import type { VRM } from "@pixiv/three-vrm";
import {
  createVRMAnimationClip,
  VRMAnimationLoaderPlugin,
} from "@pixiv/three-vrm-animation";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";
import type { AnimationIntent } from "./animationIntent";

export type AnimationAssetMap = Partial<Record<AnimationIntent,string>>;

export type VrmAnimationRuntime = {
  mixer: AnimationMixer;
  play: (intent: AnimationIntent, fadeSeconds?: number) => Promise<boolean>;
  update: (deltaSeconds: number) => void;
  dispose: () => void;
};

export const createVrmAnimationRuntime = (
  vrm: VRM,
  assets: AnimationAssetMap,
): VrmAnimationRuntime => {
  const loader=new GLTFLoader();
  loader.register(parser=>new VRMAnimationLoaderPlugin(parser));
  const mixer=new AnimationMixer(vrm.scene);
  const actions=new Map<AnimationIntent,AnimationAction>();
  let active:AnimationAction|undefined;

  const play=async(intent:AnimationIntent,fadeSeconds=.22)=>{
    const url=assets[intent];
    if(!url) return false;

    let action=actions.get(intent);
    if(!action){
      const gltf=await loader.loadAsync(url);
      const animation=gltf.userData.vrmAnimations?.[0];
      if(!animation) return false;
      const clip=createVRMAnimationClip(animation,vrm);
      action=mixer.clipAction(clip);
      actions.set(intent,action);
    }

    if(active===action) return true;
    active?.fadeOut(fadeSeconds);
    action.reset().fadeIn(fadeSeconds).play();
    active=action;
    return true;
  };

  return {
    mixer,
    play,
    update:(deltaSeconds:number)=>mixer.update(deltaSeconds),
    dispose:()=>mixer.stopAllAction(),
  };
};
