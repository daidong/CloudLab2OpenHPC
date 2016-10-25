import geni.portal as portal
import geni.rspec.pg as pg

# Create the Portal context
pc = portal.Context()

# Describe the parameter this profile script can accept
pc.defineParameter("n", "Number of Raw machines", portal.ParameterType.INTEGER, 1)
pc.defineParameter("i", "Machine Image", portal.ParameterType.INTEGER, 1)

# Retrieve the values the user specifies during instantiation
params = pc.bindParameters()

# Create a Request object to start building the RSpec
rspec = pg.Request()

# Check parameter validity
if params.n < 1 or params.n > 128:
    pc.reportError(portal.ParameterError( "You must choose from 1 to 128"))

# Check parameter for image
if params.i == 0:
    disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU12-64-STD"
else:
    disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS71-64-STD"

# Create nodes and links
link = pg.LAN("lan")

for i in range (params.n):
    node = pg.RawPC("node"+str(i))
    node.hardware_type = "r320"
    node.disk_image=disk_image
    bs = node.Blockstore("bs", "/local")
    bs.size = "60GB"

    rspec.addResource(node)
    iface = node.addInterface("if"+str(i))
    link.addInterface(iface)
    node.addService(pg.Install(url="http://myweb.ttu.edu/ddai/codes/tool.tar.gz", path="/local"))
    node.addService(pg.Execute(shell="bash", command="/local/CloudLab2OpenHPC/install.sh"))
    
rspec.addResource(link)

pc.printRequestRSpec(rspec)