/****** Object:  Table [dbo].[CustomerNames]    Script Date: 2024/05/30 10:32:47 ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[CustomerNames]') AND type in (N'U'))
DROP TABLE [dbo].[CustomerNames]
GO

/****** Object:  Table [dbo].[CustomerNames]    Script Date: 2024/05/30 10:32:47 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[CustomerNames](
	[nameId] [int] IDENTITY(1,1) NOT NULL,
	[name] [varchar](100) NULL UNIQUE,
	[nameCount] [int] NULL,
 CONSTRAINT [PK_CustomerNames] PRIMARY KEY CLUSTERED 
(
	[nameId] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


/****** Object:  Table [dbo].[CustomerSurnames]    Script Date: 2024/05/30 10:32:59 ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[CustomerSurnames]') AND type in (N'U'))
DROP TABLE [dbo].[CustomerSurnames]
GO

/****** Object:  Table [dbo].[CustomerSurnames]    Script Date: 2024/05/30 10:32:59 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[CustomerSurnames](
	[surnameId] [int] IDENTITY(1,1) NOT NULL,
	[surname] [varchar](100) NULL UNIQUE,
	[surnameCount] [int] NULL,
 CONSTRAINT [PK_CustomerSurnames] PRIMARY KEY CLUSTERED 
(
	[surnameId] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO




