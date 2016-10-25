import geni.portal as portal
import geni.rspec.pg as pg

# Create the Portal context
pc = portal.Context()

# Describe the parameter this profile script can accept
pc.defineParameter("n", "Number of Raw machines", portal.ParameterType.INTEGER, 1)
pc.defineParameter("i", "Machine Image: 0 is Ubuntu 12.04; 1 is Centos 7.1", portal.ParameterType.INTEGER, 1)

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

# Add install and execute
install = pg.Install(url="http://myweb.ttu.edu/ddai/codes/tool.tar.gz", path="/local")
execute = pg.Execute(shell="bash", command="/local/CloudLab2OpenHPC/install.sh")

for i in range (params.n):
    node = pg.RawPC("node"+str(i))
    node.hardware_type = "r320"
    node.disk_image=disk_image
    bs = node.Blockstore("bs", "/local")
    bs.size = "60GB"
    node.addService(install)
    node.addService(execute)
    
    iface = node.addInterface("if"+str(i))
    link.addInterface(iface)
    rspec.addResource(node)

    
rspec.addResource(link)

pc.printRequestRSpec(rspec)