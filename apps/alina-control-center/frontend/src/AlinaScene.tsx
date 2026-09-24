import { Canvas, useFrame } from "@react-three/fiber";
import { Suspense, useEffect, useRef, useState } from "react";
import type { Group } from "three";
import type { VRM } from "@pixiv/three-vrm";
import { alinaHumanAgentProfile } from "./humanAgentProfile";
import { loadVrmAvatar } from "./vrmAvatarLoader";
import { initialLocomotionState, requestMove, stepLocomotion, type LocomotionState } from "./locomotionController";

const canRenderWebGL = () => typeof window !== "undefined" && typeof window.ResizeObserver !== "undefined" && typeof window.WebGLRenderingContext !== "undefined";

export const sceneAnchors = {
  WORK_TABLE:[0,0,1.8],
  INFORMATION_WALL:[0,0,-2.7],
  KNOWLEDGE_PANEL:[-2.2,1.65,-2.82],
  GRAPH_PANEL:[0,1.65,-2.82],
  EVIDENCE_PANEL:[2.2,1.65,-2.82],
} as const;

function Anchor({position,label}:{position:readonly [number,number,number];label:string}){
  return <group position={[...position]}>
    <mesh position={[0,.08,0]}><cylinderGeometry args={[.14,.14,.03,24]}/><meshStandardMaterial emissive="#2de7ff" emissiveIntensity={2} color="#0a6372"/></mesh>
    <mesh position={[0,.28,0]}><boxGeometry args={[.03,.4,.03]}/><meshStandardMaterial color="#2de7ff"/></mesh>
    <mesh position={[0,.52,0]}><boxGeometry args={[.45,.16,.02]}/><meshStandardMaterial color="#08202a" emissive="#0b8195" emissiveIntensity={.8}/></mesh>
  </group>
}

function AlinaAvatar(){
  const [vrm,setVrm]=useState<VRM|null>(null);
  const [locomotion,setLocomotion]=useState<LocomotionState>(()=>initialLocomotionState());
  const locomotionRef=useRef(locomotion);
  const groupRef=useRef<Group>(null);
  const [failed,setFailed]=useState(false);

  useEffect(()=>{
    let active=true;
    let loaded:VRM|null=null;
    loadVrmAvatar(alinaHumanAgentProfile.avatar.uri)
      .then((next)=>{ loaded=next; if(active) setVrm(next); })
      .catch(()=>{ if(active) setFailed(true); });
    return ()=>{ active=false; loaded?.scene.removeFromParent(); };
  },[]);

  useEffect(()=>{ locomotionRef.current=locomotion; },[locomotion]);
  useFrame((_,delta)=>{
    const next=stepLocomotion(locomotionRef.current,delta);
    locomotionRef.current=next;
    if(groupRef.current){
      groupRef.current.position.set(...next.position);
      groupRef.current.rotation.y=next.yaw;
    }
    if(next!==locomotionRef.current) setLocomotion(next);
  });

  const moveToWall=()=>{
    const next=requestMove(locomotionRef.current,"INFORMATION_WALL");
    locomotionRef.current=next;
    setLocomotion(next);
  };

  if(failed) return <mesh position={[0,1,1.25]}><capsuleGeometry args={[.32,1.2,8,16]}/><meshStandardMaterial color="#173844" emissive="#0b8195" emissiveIntensity={.35}/></mesh>;
  if(!vrm) return null;

  return <group ref={groupRef} position={[...locomotion.position]} rotation={[0,locomotion.yaw,0]} scale={1.05} onClick={moveToWall}>
    <primitive object={vrm.scene}/>
  </group>;
}

function Room(){
  return <>
    <ambientLight intensity={.45}/>
    <directionalLight position={[4,7,5]} intensity={1.5}/>
    <pointLight position={[0,3,-1]} intensity={20} distance={8}/>
    <mesh rotation={[-Math.PI/2,0,0]} receiveShadow><planeGeometry args={[12,10]}/><meshStandardMaterial color="#071117" roughness={.85}/></mesh>
    <mesh position={[0,2.2,-3]}><boxGeometry args={[8,4.4,.18]}/><meshStandardMaterial color="#071820" metalness={.35} roughness={.55}/></mesh>
    <mesh position={[0,.65,1.9]}><boxGeometry args={[4.5,.18,1.35]}/><meshStandardMaterial color="#0a2630" metalness={.6} roughness={.35}/></mesh>
    {(["KNOWLEDGE_PANEL","GRAPH_PANEL","EVIDENCE_PANEL"] as const).map((key,i)=><mesh key={key} position={[sceneAnchors[key][0],sceneAnchors[key][1],sceneAnchors[key][2]]}>
      <boxGeometry args={[1.75,1.15,.08]}/><meshStandardMaterial color="#092630" emissive={i===1?"#0b6f84":"#063a48"} emissiveIntensity={.65}/></mesh>)}
    {Object.entries(sceneAnchors).map(([label,position])=><Anchor key={label} label={label} position={position}/>)}
  </>;
}

export function AlinaScene(){
  if (!canRenderWebGL()) {
    return <div className="scene3d scene3d-fallback" aria-label="ALINA 3D WORLD" data-renderer="fallback">
      <div className="scene3d-legend">3D WORLD · RENDERER FALLBACK · WORKSPACE REMAINS AVAILABLE</div>
    </div>;
  }

  return <div className="scene3d" aria-label="ALINA 3D WORLD" data-renderer="webgl">
    <Canvas camera={{position:[0,3.2,7.6],fov:48}} dpr={[1,1.5]}>
      <color attach="background" args={["#02070b"]}/>
      <fog attach="fog" args={["#02070b",7,16]}/>
      <Room/>
      <Suspense fallback={null}><AlinaAvatar/></Suspense>
    </Canvas>
    <div className="scene3d-legend">3D WORLD · A0 WORK TABLE · A1 INFORMATION WALL · A2–A4 PANELS</div>
  </div>;
}
