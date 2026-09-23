import Ajv from "ajv";
import { describe, expect, it } from "vitest";
import fatherObjectSchema from "../../contracts/father-object.schema.json";
import boardStateSchema from "../../contracts/board-state.schema.json";
import workspaceStateSchema from "../../contracts/workspace-state.schema.json";
import fixture from "../../fixtures/demo-workspace.json";

describe("M1 contract conformance", () => {
  const ajv = new Ajv({ allErrors: true });

  it("validates every FatherObject against its schema", () => {
    const validate = ajv.compile(fatherObjectSchema);
    for (const object of fixture.objects) {
      expect(validate(object), JSON.stringify(validate.errors)).toBe(true);
    }
  });

  it("validates every BoardState against its schema", () => {
    const validate = ajv.compile(boardStateSchema);
    for (const board of fixture.boards) {
      expect(validate(board), JSON.stringify(validate.errors)).toBe(true);
    }
  });

  it("validates WorkspaceState against its schema", () => {
    const validate = ajv.compile(workspaceStateSchema);
    expect(validate(fixture.workspace), JSON.stringify(validate.errors)).toBe(true);
  });

  it("keeps the aggregate fixture explicitly DEMO", () => {
    expect(fixture.dataStatus).toBe("DEMO");
    expect(fixture.objects.some((object) => object.dataStatus === "REAL")).toBe(false);
  });
});
