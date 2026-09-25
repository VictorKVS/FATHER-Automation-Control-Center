import type { BehaviorState } from "./presenceController";

export type AnimationIntent =
  | "IDLE_NEUTRAL"
  | "WALK_FORWARD"
  | "PRESENT_NEUTRAL"
  | "LISTEN_NEUTRAL"
  | "THINK_NEUTRAL"
  | "SPEAK_NEUTRAL"
  | "WARNING_NEUTRAL"
  | "WAIT_NEUTRAL";

export const animationIntentFor = (
  behavior: BehaviorState,
  moving: boolean,
  reducedMotion = false,
): AnimationIntent => {
  if (behavior === "WALKING" && moving) {
    return reducedMotion ? "IDLE_NEUTRAL" : "WALK_FORWARD";
  }

  switch (behavior) {
    case "PRESENTING": return "PRESENT_NEUTRAL";
    case "LISTENING": return "LISTEN_NEUTRAL";
    case "THINKING": return "THINK_NEUTRAL";
    case "SPEAKING": return "SPEAK_NEUTRAL";
    case "WARNING": return "WARNING_NEUTRAL";
    case "WAITING": return "WAIT_NEUTRAL";
    default: return "IDLE_NEUTRAL";
  }
};
