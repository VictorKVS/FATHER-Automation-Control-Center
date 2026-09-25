import { render,screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { beforeEach,describe,expect,it } from "vitest";
import App from "./App";
import { loadPresentationState, savePresentationState, WORKSPACE_STORAGE_KEY } from "./workspaceState";

describe("ALINA Control Center M1",()=>{
 beforeEach(()=>localStorage.clear());

 it("T01 renders shell without backend",()=>{render(<App/>);expect(screen.getByText(/ALINA CONTROL CENTER/)).toBeTruthy();expect(screen.getByText(/WORK TABLE/)).toBeTruthy();});
 it("T02 keeps demo truth visible",()=>{render(<App/>);expect(screen.getAllByText("DEMO").length).toBeGreaterThan(0);expect(screen.getByText(/Knowledge Core: NOT CONNECTED/)).toBeTruthy();});
 it("T03 opens board after close",async()=>{const u=userEvent.setup();render(<App/>);await u.click(screen.getByRole("button",{name:"Свернуть табло"}));await u.click(screen.getByRole("button",{name:"Открыть Knowledge"}));expect(screen.getByText("KNOWLEDGE")).toBeTruthy();});
 it("T04 toggles focus",async()=>{const u=userEvent.setup();render(<App/>);await u.click(screen.getByRole("button",{name:"Focus Mode"}));expect(screen.getByRole("button",{name:"Выйти из Focus"})).toBeTruthy();});
 it("T05 cycles ALINA presence",async()=>{const u=userEvent.setup();render(<App/>);await u.click(screen.getByRole("button",{name:/ALINA: COMPACT_3D/}));expect(screen.getByLabelText("ALINA EYES")).toBeTruthy();});
 it("T06 keeps workspace usable when avatar renderer fails",()=>{render(<App avatarRendererAvailable={false}/>);expect(screen.getByRole("status")).toHaveTextContent("RENDERER UNAVAILABLE");expect(screen.getByText(/WORK TABLE/)).toBeTruthy();});
 it("T07 restores presentation state without canonical object copies",()=>{savePresentationState({focus:true,boardOpen:false,presence:"EYES"});const restored=loadPresentationState();expect(restored).toEqual({focus:true,boardOpen:false,presence:"EYES"});expect(localStorage.getItem(WORKSPACE_STORAGE_KEY)).not.toContain("demo:document");});
 it("T09 falls back safely on corrupt persisted state",()=>{localStorage.setItem(WORKSPACE_STORAGE_KEY,"{broken");expect(loadPresentationState()).toEqual({focus:false,boardOpen:true,presence:"COMPACT_3D"});});
});
