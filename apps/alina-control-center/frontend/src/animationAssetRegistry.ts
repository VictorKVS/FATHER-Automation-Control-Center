import type { AnimationIntent } from "./animationIntent";

export type AnimationAssetRecord = {
  status: "PENDING_ASSET_REVIEW" | "LOCAL_VERIFIED";
  path: string | null;
  source: string | null;
  license: string | null;
  sha256: string | null;
};

export type AnimationManifest = {
  schema_version: string;
  agent_id: string;
  runtime_format: "VRMA";
  runtime_library: string;
  policy: string;
  assets: Partial<Record<AnimationIntent,AnimationAssetRecord>>;
};

export const isVerifiedAnimationAsset = (
  asset: AnimationAssetRecord | undefined,
): asset is AnimationAssetRecord & { path:string; source:string; license:string; sha256:string } =>
  Boolean(
    asset &&
    asset.status === "LOCAL_VERIFIED" &&
    asset.path &&
    asset.source &&
    asset.license &&
    /^[a-f0-9]{64}$/i.test(asset.sha256 ?? ""),
  );

export const verifiedAnimationMap = (
  manifest: AnimationManifest,
): Partial<Record<AnimationIntent,string>> =>
  Object.fromEntries(
    Object.entries(manifest.assets)
      .filter(([,asset])=>isVerifiedAnimationAsset(asset))
      .map(([intent,asset])=>[intent,asset!.path]),
  ) as Partial<Record<AnimationIntent,string>>;
