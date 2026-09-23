import { describe,expect,it } from "vitest";
import css from "./styles.css?raw";

describe("accessibility baseline",()=>{
 it("T08 defines a reduced-motion rendering path",()=>{
   expect(css).toContain("prefers-reduced-motion:reduce");
   expect(css).toContain("animation:none");
 });
});
