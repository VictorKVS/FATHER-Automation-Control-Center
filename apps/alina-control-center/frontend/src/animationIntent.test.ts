import { describe, expect, it } from "vitest";
import { animationIntentFor } from "./animationIntent";

describe("ALINA animation intent",()=>{
  it("maps real locomotion to walk",()=>{
    expect(animationIntentFor("WALKING",true)).toBe("WALK_FORWARD");
  });
  it("does not display walking when locomotion is not moving",()=>{
    expect(animationIntentFor("WALKING",false)).toBe("IDLE_NEUTRAL");
  });
  it("maps arrival presentation independently of locomotion",()=>{
    expect(animationIntentFor("PRESENTING",false)).toBe("PRESENT_NEUTRAL");
  });
  it("honors reduced motion without falsifying position state",()=>{
    expect(animationIntentFor("WALKING",true,true)).toBe("IDLE_NEUTRAL");
  });
  it("provides neutral intents for conversational states",()=>{
    expect(animationIntentFor("LISTENING",false)).toBe("LISTEN_NEUTRAL");
    expect(animationIntentFor("THINKING",false)).toBe("THINK_NEUTRAL");
    expect(animationIntentFor("SPEAKING",false)).toBe("SPEAK_NEUTRAL");
  });
});
