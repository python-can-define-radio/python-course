"""An example of a function that can show variables and their types with minimal effort on the user's part."""


_realprint = print  # In case print accidentally gets overwritten later
def _showvars(lcls: dict):
    yellow = "\x1b[33m"
    endcol = "\x1b[0m"
    without_undesirable = filter(lambda x: not x[0].startswith("_"), lcls.items())
    varsdisp = map(lambda x: f"│ {x[0]}: {type(x[1]).__name__} = {repr(x[1])}", without_undesirable)
    _realprint("\n")
    _realprint(f"┌────────────── {yellow}Variables{endcol} ───────────────")
    _realprint("\n".join(varsdisp))
    _realprint("└────────────────────────────────────────")
    _realprint("\n")



x = 2 + 3
_showvars(locals())
age = int(input("age: "))
oldenough = age > 7
if oldenough:
    result = "done"

_showvars(locals())
