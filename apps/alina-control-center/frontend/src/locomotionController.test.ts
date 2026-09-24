import { describe, expect, it } from "vitest";
import { initialLocomotionState, requestMove, stepLocomotion } from "./locomotionController";

describe("ALINA P3 locomotion",()=>{
  it("starts at WORK_TABLE in IDLE",()=>{
    const s=initialLocomotionState();
    expect(s.anchor).toBe("WORK_TABLE");
    expect(s.behavior).toBe("IDLE");
    expect(s.moving).toBe(false);
  });

  it("MOVE_TO information wall enters WALKING",()=>{
    const s=requestMove(initialLocomotionState(),"INFORMATION_WALL");
    expect(s.targetAnchor).toBe("INFORMATION_WALL");
    expect(s.behavior).toBe("WALKING");
    expect(s.moving).toBe(true);
  });

  it("advances toward the target without teleporting",()=>{
    const start=requestMove(initialLocomotionState(),"INFORMATION_WALL");
    const next=stepLocomotion(start,.25);
    expect(next.position).not.toEqual(start.position);
    expect(next.anchor).toBe("WORK_TABLE");
    expect(next.moving).toBe(true);
  });

  it("arrives and switches to PRESENTING",()=>{
    let s=requestMove(initialLocomotionState(),"INFORMATION_WALL");
    for(let i=0;i<1000&&s.moving;i++) s=stepLocomotion(s,.016,20);
    expect(s.anchor).toBe("INFORMATION_WALL");
    expect(s.moving).toBe(false);
    expect(s.behavior).toBe("PRESENTING");
  });

  it("same-anchor request does not create fake movement",()=>{
    const s=requestMove(initialLocomotionState(),"WORK_TABLE");
    expect(s.moving).toBe(false);
  });
});
