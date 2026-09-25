import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { VRMLoaderPlugin, VRMUtils, type VRM } from "@pixiv/three-vrm";

export async function loadVrmAvatar(uri: string): Promise<VRM> {
  const loader = new GLTFLoader();
  loader.register((parser) => new VRMLoaderPlugin(parser));
  const gltf = await loader.loadAsync(uri);
  const vrm = gltf.userData.vrm as VRM | undefined;
  if (!vrm) throw new Error(`VRM payload missing: ${uri}`);

  VRMUtils.removeUnnecessaryVertices(gltf.scene);
  VRMUtils.combineSkeletons(gltf.scene);
  VRMUtils.combineMorphs(vrm);
  vrm.scene.traverse((object) => {
    object.frustumCulled = false;
  });
  return vrm;
}
