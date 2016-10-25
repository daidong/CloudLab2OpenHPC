import geni.portal as portal
import geni.rspec.pg as pg

# Create the Portal context
pc = portal.Context()

# Describe the parameter this profile script can accept
pc.defineParameter("n", "Number of Raw machines", portal.ParameterType.INTEGER, 1)

# Retrieve the values the user specifies during instantiation
params = pc.bindParameters()

# Create a Request object to start building the RSpec
rspec = pg.Request()

# Check parameter validity
if params.n < 1 or params.n > 128:
    pc.reportError(portal.ParameterError( "You must choose from 1 to 128"))
    
# Create nodes and links
link = pg.LAN("lan")

for i in range (params.n):
    node = pg.RawPC("node"+str(i))
    node.hardware_type = "r320"
    node.disk_image="urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU12-64-STD"
    rspec.addResource(node)
    iface = node.addInterface("if"+str(i))
    link.addInterface(iface)
    
rspec.addResource(link)

pc.printRequestRSpec(rspec)