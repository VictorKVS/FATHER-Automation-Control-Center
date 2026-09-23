import { describe,expect,it } from "vitest";
import fixture from "../../fixtures/demo-workspace.json";

describe("public fixture hygiene",()=>{
 it("T10 contains no obvious secrets, PII fields, or absolute local paths",()=>{
   const text=JSON.stringify(fixture);
   expect(text).not.toMatch(/[A-Z]:\\\\/i);
   expect(text).not.toMatch(/(api[_-]?key|password|secret|token)["']?\s*:/i);
   expect(text).not.toMatch(/(passport|snils|email|phone|full_name)["']?\s*:/i);
 });
});
