import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";

describe("accessibility baseline",()=>{
 it("T08 defines a reduced-motion rendering path",()=>{
   const css = readFileSync(resolve(process.cwd(), "src/styles.css"), "utf8");
   expect(css).toContain("prefers-reduced-motion:reduce");
   expect(css).toContain("animation:none");
 });
});
