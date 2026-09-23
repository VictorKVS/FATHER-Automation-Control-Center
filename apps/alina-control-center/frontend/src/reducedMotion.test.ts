import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { describe, expect, it } from "vitest";

describe("accessibility baseline",()=>{
 it("T08 defines a reduced-motion rendering path",()=>{
   const cssPath = fileURLToPath(new URL("./styles.css", import.meta.url));
   const css = readFileSync(cssPath, "utf8");
   expect(css).toContain("prefers-reduced-motion:reduce");
   expect(css).toContain("animation:none");
 });
});
